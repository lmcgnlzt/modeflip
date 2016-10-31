from datetime import datetime

from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import Bool, String, EmbeddedObject
from modeflip.utils.valid_model_utils import DateTime, Integer, Float

from modeflip.models.transaction import Transaction
from modeflip.models.common import Video, Music


class Scene(Object):
	sid = Integer(nullable=False)
	merchant_name = String(mutator=lambda x: x.strip(), nullable=False) # user_name of Merchant
	transaction = EmbeddedObject(Transaction)
	qr_code_url = String()
	scanned = Bool(default=False) # important to mark as True after used/scanned



class SceneConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['scenes']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('sid', 1)], unique=True)
		self.collection.ensure_index([('merchant_name', 1), ('sid', -1)])

	def get(self, sid):
		doc = self.collection.find_one({'sid': sid}, {'_id': 0})
		return Scene(**doc) if doc else None

	def get_next_available_id(self):
		try:
			return list(self.collection.find({}, {'sid': 1}, sort=[('sid', -1)], limit=1))[0]['sid'] + 1
		except IndexError:
			return 1

	def get_all_ids(self):
		return [c['sid'] for c in self.collection.find({}, {'_id': 0, 'sid': 1})]

	def get_by_merchant_name(self, merchant_name):
		return [Scene(**doc) for doc in self.collection.find({'merchant_name': merchant_name}, {'_id': 0}).sort('sid', -1)]

	def set(self, scene):
		scene.validate()
		self.collection.update({'sid': scene.sid}, scene.__json__(), safe=True, upsert=True)
		return scene

	def delete(self, sid):
		scene = self.get(sid)
		if scene:
			self.collection.remove({'sid': sid})
			return True
		return False