from datetime import datetime
from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, Integer, List, DateTime


class Collection(Object):
	cid = Integer(nullable=False)
	did = Integer(nullable=False)
	name = String(nullable=False)
	released = DateTime(nullable=False)
	signatrue_pics = List()
	signatrue_musics = List()
	signatrue_videos = List()

	def __init__(self, **kwargs):
		released = kwargs.get('released')
		if isinstance(released, unicode):
			released = datetime.strptime(released, '%Y-%m-%d')
		kwargs['released'] = released
		Object.__init__(self, **kwargs)


class CollectionConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['collections']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1), ('cid', 1)])

	def get(self, did, cid):
		doc = self.collection.find_one({'did': did, 'cid': cid}, {'_id': 0})
		return Collection(**doc) if doc else None

	def get_all_collections_by_designer(self, did):
		return [Collection(**doc) for doc in self.collection.find({'did': did}, {'_id': 0}).sort('released', -1)]

	def set(self, collection):
		collection.validate()
		self.collection.update({'cid': collection.cid, 'did': collection.did}, collection.__json__(), safe=True, upsert=True)
		return collection

	def delete(self, did, cid):
		collection = self.get(did, cid)
		if collection:
			self.collection.remove({'did': did, 'cid': cid})
			return True
		return False