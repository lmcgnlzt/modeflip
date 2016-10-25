#coding=utf-8

import json
import requests
from datetime import datetime
from pyramid.httpexceptions import exception_response
from modeflip.models.merchant import Merchant, MerchantConfig
from modeflip.models.member import Member, MemberConfig
from modeflip.models.item import Item, ItemConfig
from modeflip.models.transaction import Transaction, TransactionConfig
from modeflip.models.scene import Scene, SceneConfig
from modeflip.utils.date_utils import unix_timestamp_int_in_seconds

from pprint import pprint

import logging
LOGGER = logging.getLogger(__name__)


class MembershipAPI(object):

	MERCHANT_OPENID = 'merchants:{open_id}'

	def __init__(self, context, request):
		self.request = request
		config_db = request.get_database('mf_config')
		self.cache = request.get_cache('mf_cache')
		self.mc = MerchantConfig(config_db)
		self.mbc = MemberConfig(config_db)
		self.ic = ItemConfig(config_db)
		self.tc = TransactionConfig(config_db)
		self.sc = SceneConfig(config_db)

	# POST /membership_api/merchant/login
	def merchant_login(self):
		try:
			data = self.request.json_body
			password_verified = self.mc.get_by_password(data['user_name'], data['plaintext_passwd'])
			if not password_verified:
				return False
			else:
				open_id = data['open_id']
				now = datetime.utcnow()
				key = self.MERCHANT_OPENID.format(open_id=open_id)
				self.cache.set(key, unix_timestamp_int_in_seconds(now))
				LOGGER.warning('[Login recorded] open_id [%s] logged in at [%s]', open_id, now)
				return True

		except Exception as e:
			LOGGER.exception(e)
			return False

	# GET /membership_api/merchant/items/tags
	def merchant_item_tags(self):
		return self.ic.get_all_tags()

	# GET /membership_api/merchant/{open_id}/authorized
	def merchant_authorized(self):
		open_id = self.request.matchdict['open_id']



		open_id = 'olBwZt_NW0IBseUIa5fImCCj_dn4'



		# key = 'merchants:{}'.format(open_id)
		key = self.MERCHANT_OPENID.format(open_id=open_id)
		return self.cache.exists(key) and (unix_timestamp_int_in_seconds(datetime.utcnow()) - int(self.cache.get(key))) > 30 # 8 Hours

	# GET /membership_api/merchant/items/{tag}
	def merchant_item(self):
		tag = self.request.matchdict['tag']
		tag = tag.strip().upper()
		return self.ic.get_by_tag(tag)

	# POST /membership_api/merchant/generate
	def merchant_generate(self):
		'''
		scene_id: 1~10000,
		recognize key for qrcode scan?
		scene_id : real_scene_id, real_scene_id : scene object

		'''
		try:
			data = self.request.json_body
			merchant_name = data['merchant_name']
			LOGGER.warning('Merchant action started. [%s]', merchant_name)
			items = data['items']

			# persist transaction
			trans = self.tc.set(
				Transaction(
					tid=self.tc.get_next_available_id(),
					merchant_name=merchant_name,
					items=items,
				)
			)
			LOGGER.warning('[Transaction recorded] trans_id: %s. [%s]', trans.tid, trans.merchant_name)

			# persist scene
			scene = self.sc.set(
				Scene(
					scene_id='TRANSACTION-{}'.format(trans.tid), # IMPORTANT prefix for wechant scan POST event
					merchant_name=merchant_name,
					transaction=trans
				)
			)
			LOGGER.warning('[Scene recorded] scene_id: %s. [%s]', scene.scene_id, scene.merchant_name)

			# post to get QR code
			ticket_url = self.request.registry['wechat_qrcode_endpoint'].format(access_token=self.cache.get('access_token'))
			body = {"expire_seconds": 259200, "action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": scene.scene_id}}} # TTL 3 days
			res = requests.post(ticket_url, data=json.dumps(body))
			qr_ticket = res.json()['ticket']
			qr_image_url = self.request.registry['qrcode_image_url'].format(ticket=qr_ticket)
			LOGGER.warning('[QRCode generated] request completed with [%s], scene_id: %s, QR image url: [%s]. [%s]', res.status_code, scene.scene_id, qr_image_url, merchant_name)

			# update scene object
			scene.qr_code_url = qr_image_url
			self.sc.set(scene)
			LOGGER.warning('Merchant action completed. [%s]', merchant_name)

			return qr_image_url

		except Exception as e:
			LOGGER.exception(e)
			return None

	# POST /membership_api/member/scan
	def member_scan(self):
		'''
		upon user scan:
		- get scene by scene_id
		- check if scanned already
		- update transaction open_id
		- update scene scanned
		- update member shopping_history with new transaction
		- notify member points earned
		'''

		try:
			data = self.request.json_body
			scene_id = data['scene_id']
			scanner_open_id = data['scanner_open_id']
			scene = self.sc.get(scene_id)

			# check if scanned already
			if scene.scanned:
				body = {
				    "touser": scanner_open_id,
				    "msgtype": "text",
				    "text":
					    {
					         "content": u"二维码已无效，无法再次识别"
					    }
					}
				status_code = self._notify_user(body)
				LOGGER.warning('[QRCode repeat scan] by open_id %s. Scene_id: %s. Warning message sent [%s].', scanner_open_id, scene_id, status_code)
				return

			# update transaction open_id
			transaction = scene.transaction
			transaction.open_id = scanner_open_id
			trans = self.tc.set(transaction)
			LOGGER.warning('[Transaction linked] transaction_id: %s with open_id: %s. [%s]', trans.tid, trans.open_id, trans.merchant_name)

			# update scene scanned
			scene.scanned = True
			s = self.sc.set(scene)
			LOGGER.warning('[QR code marked as scanned] scene_id: %s. [%s]', s.scene_id, s.merchant_name)

			# update member history
			member = self.mbc.get(scanner_open_id)
			if member is not None:
				member.shopping_history.insert(0, trans)
				member.last_updated_on = datetime.utcnow()
				mb = self.mbc.set(member)
			else:
				mb = self.mbc.set(
					Member(
						open_id=scanner_open_id,
						last_updated_on=datetime.utcnow(),
						shopping_history=[trans],
						)
					)
			LOGGER.warning('[Shopping history updated] for member %s (member since %s, last updated on %s)', mb.open_id, mb.created_on, mb.last_updated_on)

			# notify member points earned
			body = {
			    "touser": scanner_open_id,
			    "msgtype": "text",
			    "text":
				    {
				         "content": u"恭喜您获得线下消费积分奖励，目前您的总消费积分为 {}。(积分使用及相关活动请咨询MODEFLIP线下实体店)".format(mb.total_points)
				    }
				}
			status_code = self._notify_user(body)
			LOGGER.warning('[Member newly earned points notified]')

		except Exception as e:
			LOGGER.exception(e)

	def _notify_user(self, payload):
		messaging_url = self.request.registry['message_to_client_endpoint'].format(access_token=self.cache.get('access_token'))
		try:
			res = requests.post(messaging_url, data=json.dumps(payload, ensure_ascii=False).encode('utf8'))
			return res.status_code
		except Exception as e:
			LOGGER.exception('Message to client failed')
			return '500'


def add_view(config, route_name, method, attr):
	handler = 'modeflip.api_internal.membership_api:MembershipAPI'
	config.add_view(
		handler,
		attr=attr,
		route_name=route_name,
		request_method=method,
		renderer='json'
		)


def includeme(config):
	"""
	merchant login
	- menu click
	- get open_id
	- check:
		if open_id exists and delta < 8 hours:
			- find merchant by open_id
		else:
			- show login page
			- after login, store open_id : utcnow

	(session data: open_id as key, last_time_login as value)


	find item(s) by tag(s) (prefix search)
	get_all_tags (then autocomplete as user enter)

	press generate:
	- create transaction
	- create Scene object with id and persist, scene_id : {merchant_name + transaction}
	- post to generate QR code
	- update scene object
	- return QR image url
	persist , QR_url. Return QR_url


	upon user scan:
	- get scene by scene_id
	- check if scanned already
	- update transaction open_id
	- update scene scanned
	- get&update or create member shopping_history with new transaction
	- notify member points earned
	"""
	config.add_route('merchant_login', '/membership_api/merchant/login')
	add_view(config, 'merchant_login', 'POST', 'merchant_login')

	config.add_route('merchant_authorized', '/membership_api/merchant/{open_id}/authorized')
	add_view(config, 'merchant_authorized', 'GET', 'merchant_authorized')

	config.add_route('merchant_item_tags', '/membership_api/merchant/items/tags')
	add_view(config, 'merchant_item_tags', 'GET', 'merchant_item_tags')

	config.add_route('merchant_item', '/membership_api/merchant/items/{tag}')
	add_view(config, 'merchant_item', 'GET', 'merchant_item')

	config.add_route('merchant_generate', '/membership_api/merchant/generate')
	add_view(config, 'merchant_generate', 'POST', 'merchant_generate')

	config.add_route('member_scan', '/membership_api/member/scan')
	add_view(config, 'member_scan', 'POST', 'member_scan')