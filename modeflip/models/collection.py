from datetime import datetime
from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject, Bool
from modeflip.utils.valid_model_utils import Integer, DateTime

from modeflip.models.common import Video, Music
from modeflip.models.garment import Garment


class Collection(Object):
	cid = Integer(nullable=False)
	did = Integer(nullable=False)
	title = String()
	desc = String()
	released = DateTime(nullable=False)
	signatrue_pics = List(value=String(), validator=lambda x: all('/' in i for i in x))
	signatrue_videos = List(value=EmbeddedObject(Video))
	signatrue_musics = List(value=EmbeddedObject(Music))
	new_arrival = Bool(default=False)
	garments = List(value=EmbeddedObject(Garment)) # place holder for data transformation

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
		self.collection.ensure_index([('released', -1)])

	def get(self, did, cid):
		doc = self.collection.find_one({'did': did, 'cid': cid}, {'_id': 0})
		return Collection(**doc) if doc else None

	def get_all_ids(self, did):
		return [c['cid'] for c in self.collection.find({'did': did}, {'_id':0, 'cid':1}).sort('cid', 1)]

	def get_all_collections_by_designer(self, did):
		return [Collection(**doc) for doc in self.collection.find({'did': did}, {'_id': 0}).sort('released', -1)]

	def get_latest_collections_by_designer(self, did, limit=2):
		return [Collection(**doc) for doc in self.collection.find({'did': did}, {'_id': 0}).sort('released', -1).limit(limit)]

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