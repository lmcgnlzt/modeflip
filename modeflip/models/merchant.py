from datetime import datetime
import bcrypt

from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import DateTime, Integer
from modeflip.utils.math_utils import generate_random_key

# from modeflip.models.transaction import Transaction


class Merchant(Object):
	user_name = String(mutator=lambda x: x.strip(), nullable=False)
	passwd = String(default=generate_random_key)
	salty_passwd = String()

	wechat_id = String(nullable=False) # this might change over time
	address = String()
	phone = String()

	created_on = DateTime(datetime.utcnow())
	# sales_history = List(value=EmbeddedObject(Transaction)) # bad idea to keep sales history on merchant?


	def check_salted_password(self, plaintext_passwd):
		if isinstance(plaintext_passwd, unicode):
			plaintext_passwd = plaintext_passwd.encode('utf8')
		if self.salty_passwd is None:
			return False
		return bcrypt.checkpw(plaintext_passwd, self.salty_passwd)

	def set_password(self, plaintext_passwd):
		if isinstance(plaintext_passwd, unicode):
			plaintext_passwd = plaintext_passwd.encode('utf8')
		salted_password = bcrypt.hashpw(plaintext_passwd, bcrypt.gensalt())
		self.salty_passwd = salted_password
		self.passwd = None



class MerchantConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['merchants']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('user_name', 1)], unique=True)
		self.collection.ensure_index([('wechat_id', 1)])

	def get_by_user_name(self, user_name):
		doc = self.collection.find_one({'user_name': user_name}, {'_id': 0})
		return Merchant(**doc) if doc else None

	def get_by_wechat_id(self, wechat_id):
		doc = self.collection.find_one({'wechat_id': wechat_id}, {'_id': 0})
		return Merchant(**doc) if doc else None

	# get by user entered user_name & password, if all info matches, then return object
	def get_by_password(self, user_input, plaintext_passwd):
		merchant = self.get_by_user_name(user_input) or self.get_by_wechat_id(user_input)
		if merchant is None:
			return None

		if merchant.check_salted_password(plaintext_passwd):
			return merchant

		return None

	def set(self, merchant):
		merchant.validate()
		self.collection.update({'user_name': merchant.user_name}, merchant.__json__(), safe=True, upsert=True)
		return merchant

	def delete(self, user_name):
		merchant = self.get_by_user_name(user_name)
		if merchant:
			self.collection.remove({'user_name': user_name})
			return True
		return False