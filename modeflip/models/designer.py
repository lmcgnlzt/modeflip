from modeflip.valid_model import Object, ValidationError
from modeflip.valid_model.descriptors import String, Bool, Bool, Integer, List, Dict, EmbeddedObject


class Designer(Object):
	did = Integer(nullable=False)
	name = String(nullable=False, validator=lambda x: x and len(x) >0)
	origin = String(mutator=lambda x: x.strip().upper())
	icon = String()
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
	def get_collections(self, did):
		designer = self.get(did)
		return designer.collections if designer else []

	def get_collection_by_id(self, did, cid):
		designer = self.get(did)
		if designer:
			# result = self.collection.find_one({'did': did, 'collections.cid': cid}, {'collections': 1})
			result = self.collection.find_one({'did': did, 'collections.cid': cid}, {'collections.$': 1})
			# pprint(result)

			q = {'did': did, 'collections': {'$elemMatch': {'cid': cid}}}
			p = {'collections.cid': 0, 'collections': {'$elemMatch': {'cid': cid}}}
			ret = self.collection.find_one(q, p)
			pprint(ret)
			# print type(result)
			# pprint(result.explain())
			# if result and result['collections']:
				# return Collection(**result['collections'][0])

	def get_outfits(self, did, cid):
		collection = self.get_collection_by_id(did, cid)
		return collection.outfits if collection else []

	def get_outfit_by_id(self, did, cid, oid):
		designer = self.get(did)
		if designer:
			# result = self.collection.find_one({'did': did, 'collections.cid': cid, 'collections.outfits.oid': oid}, {'collections.outfits': 1})
			# result = self.collection.find_one({'did': did, 'collections.cid': cid, 'collections.outfits.oid': oid}, {'collections.outfits.$': 1})
			result = self.collection.find_one({'collections.outfits': {'$elemMatch': {'oid': oid}}}, {'collections.outfits.$': 1})

			'''
			db.mycollection.find({
			    "did": {
			        "$elemMatch": {
			            "name": "name1",
			            "someNestedArray": {
			                "$elemMatch": {
			                    "name": "value",
			                    "otherField": 1
			                }
			            }
			        }
			    }
			})
			'''

			# print result['collections'], '???'
			pprint(result)
			# if result and result['collections']:
			# 	return Outfit(**result['collections'][0]['outfits'])
	"""


"""
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






"""
First trial:


Designer
 - did
 - name
 - city
 - is_active
 - bio
 - likes
 - subscribers
 - music_collection
 - collections
 	- collection1 (monthly)
 		- name
 		- signatrue_pic
 		- signatrue_music
 		- signatrue_video
 		- outfit1
 			- oid
 			- pics [pic1, pic2, pic3]
 			- description
 		- outfit2


 	- collection2
"""