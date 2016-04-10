import logging
import traceback
import json
import time
from datetime import datetime, timedelta
from bson import ObjectId
from pyramid.httpexceptions import exception_response, HTTPError, HTTPException
from pyramid.tweens import EXCVIEW
from zope.interface import implementer
from pyramid.interfaces import ISession
import binascii
import os
from pyramid.compat import text_

class BadCSRFToken(Exception):
	pass

class XSSException(Exception):
	pass

def _build_stat_name(request):
	route_name = request.matched_route.name if request.matched_route else 'None'
	parts = [request.method, route_name]
	stat = '-'.join(parts)
	return stat

def default_json_encoder(obj):
	if isinstance(obj, unicode):
		return obj.encode('utf-8')
	elif isinstance(obj, datetime):
		if obj.tzinfo == None:
			return obj.strftime("%Y-%m-%dT%H:%M:%SZ")
		else:
			return obj.strftime("%Y-%m-%dT%H:%M:%S%z")
	elif isinstance(obj, timedelta):
		return obj.total_seconds()
	elif isinstance(obj, set):
		return list(obj)
	elif callable(getattr(obj, '__json__', False)):
		return obj.__json__()
	elif isinstance(obj, ObjectId):
		return str(obj)
	raise TypeError(type(obj)) # pragma: no cover

def json_renderer_factory(_):
	def _render(value, system):
		request = system.get('request')
		if request is not None:
			response = request.response
			if response.content_type == response.default_content_type:
				response.content_type = 'application/json'
		return json.dumps(value, default=default_json_encoder)

	return _render

def jsonp_renderer_factory(_):
	"""A special renderer which returns JSONP data.
	Be careful to only return data that can be dumped to JSON. In particular
	unicode strings may not work.
	"""
	def _render(value, system):
		request = system.get("request")
		callback = request.params["callback"]
		request.response_content_type = "application/json"
		return "{}({})".format(callback, json.dumps(value, default=default_json_encoder))

	return _render

def _dummy_func(_):
	pass

def add_request_methods(config):
	get_cache = config.registry.get('get_cache', _dummy_func)
	get_database = config.registry.get('get_database', _dummy_func)
	config.add_request_method(lambda _r, cache: get_cache(cache), 'get_cache')
	config.add_request_method(lambda _r, db: get_database(db), 'get_database')
	config.add_request_method(set_csrf_token, 'set_csrf_token')
	config.add_request_method(check_csrf_token, 'check_csrf_token')

@implementer(ISession)
class InMemorySession(dict):
	_flash_queue_prefix = '_f_'
	def __init__(self, **values):
		super(InMemorySession, self).__init__(**values)
		self._created = int(time.time())
		self._changed = False
		self._new = True

	def invalidate(self):
		self.clear()

	def flash(self, msg, queue='', allow_duplicate=True):
		flash_queue_key = self._flash_queue_prefix + queue
		msg_queue = self.setdefault(flash_queue_key, [])
		if allow_duplicate or msg not in msg_queue:
			msg_queue.append(msg)
			self.changed()

	@property
	def created(self):
		return self._created

	def changed(self):
		self._changed = True

	def get_csrf_token(self):
		token = self.get('_csrft_', None)
		if token is None:
			token = self.new_csrf_token()
		else:
			token = unicode(token)
		return token

	def peek_flash(self, queue=''):
		flash_queue_key = self._flash_queue_prefix + queue
		return self.get(flash_queue_key, [])

	def new_csrf_token(self):
		token = text_(binascii.hexlify(os.urandom(20)))
		self['_csrft_'] = token
		return token

	@property
	def new(self):
		return self._new

	def pop_flash(self, queue=''):
		flash_queue_key = self._flash_queue_prefix + queue
		self.changed()
		return self.pop(flash_queue_key, [])


def set_csrf_token(request):
	token = request.session.new_csrf_token()
	request.response.headers['X-CSRF-Token'] = str(token)

def check_csrf_token(request):
	supplied_token = request.headers.get('X-CSRF-Token')
	if supplied_token != request.session.get_csrf_token():
		raise BadCSRFToken('check_csrf_token(): Invalid token')
	return True

def InMemorySessionFactory(request):
	return InMemorySession()

def includeme(config):
	config.include(add_request_methods)
	config.add_renderer('json', json_renderer_factory)
	config.add_renderer('jsonp', jsonp_renderer_factory)
