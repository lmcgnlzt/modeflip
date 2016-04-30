from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, Bool, List
from modeflip.utils.valid_model_utils import Integer


class Designer(Object):
	did = Integer(nullable=False)
	name = String(nullable=False, validator=lambda x: x and len(x) >0)
	origin = String(mutator=lambda x: x.strip().upper())
	icon_link = String()
	is_active = Bool(default=False)
	bio = String()
	likes = Integer(default=0)
	subscribers = Integer(default=0)
	music_collection = List()


class DesignerConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['designers']

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1)])
		self.collection.ensure_index([('name', 1)])
		self.ensure_indexes()

	def get(self, did):
		doc = self.collection.find_one({'did': did}, {'_id': 0})
		return Designer(**doc) if doc else None

	def get_all_designers(self):
		return [Designer(**doc) for doc in self.collection.find({}, {'_id': 0}).sort('name', 1)]

	def get_designers_by_page(self, _page=1, _perPage=10):
		return [Designer(**doc) for doc in self.collection.find({'did': {'$gt': (_page-1)*_perPage, '$lte': _page*_perPage}}, {'_id': 0}).sort('name', 1)]

	def set(self, designer):
		designer.validate()
		self.collection.update({'did': designer.did}, designer.__json__(), safe=True, upsert=True)
		return designer

	def get_likes(self, did):
		result = self.collection.find_one({'did': did}, {'likes': 1, '_id': 0})
		return result['likes'] if result else None

	def do_like(self, did):
		curr_likes = self.get_likes(did)
		if curr_likes is not None:
			self.collection.update({'did': did}, {'$inc': {'likes': 1}})
			return curr_likes + 1

	def get_subscribes(self, did):
		result = self.collection.find_one({'did': did}, {'subscribers': 1, '_id': 0})
		return result['subscribers'] if result else None

	def do_subscribe(self, did):
		curr_subscribes = self.get_subscribes(did)
		if curr_subscribes is not None:
			self.collection.update({'did': did}, {'$inc': {'subscribers': 1}})
			return curr_subscribes + 1

	def delete(self, did):
		designer = self.get(did)
		if designer:
			self.collection.remove({'did': did})
			return True
		return False



"""
Final Model:

Designer
 - did
 - name
 - origin
 - icon
 - is_active
 - bio
 - likes
 - subscribers
 - music_collection


Collection
 - cid
 - did
 - name
 - released
 - signatrue_pic (many)
 - signatrue_music (many)
 - signatrue_video (many)


Garment
 - gid
 - cid
 - did
 - price
 - description
 - pictures
"""