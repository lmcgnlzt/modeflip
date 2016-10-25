from datetime import datetime

from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import Bool, String, EmbeddedObject
from modeflip.utils.valid_model_utils import DateTime, Integer, Float

from modeflip.models.transaction import Transaction
from modeflip.models.common import Video, Music


class Scene(Object):
	scene_id = String(nullable=False, validator=lambda x: x.startswith('TRANSACTION-'))
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
		self.collection.ensure_index([('scene_id', 1)], unique=True)
		self.collection.ensure_index([('merchant_name', 1), ('scene_id', -1)])

	def get(self, scene_id):
		doc = self.collection.find_one({'scene_id': scene_id}, {'_id': 0})
		return Scene(**doc) if doc else None

	def get_all_ids(self):
		return [c['scene_id'] for c in self.collection.find({}, {'_id': 0, 'scene_id': 1})]

	def get_by_merchant_name(self, merchant_name):
		return [Scene(**doc) for doc in self.collection.find({'merchant_name': merchant_name}, {'_id': 0}).sort('scene_id', -1)]

	def set(self, scene):
		scene.validate()
		self.collection.update({'scene_id': scene.scene_id}, scene.__json__(), safe=True, upsert=True)
		return scene

	def delete(self, scene_id):
		scene = self.get(scene_id)
		if scene:
			self.collection.remove({'scene_id': scene_id})
			return True
		return False