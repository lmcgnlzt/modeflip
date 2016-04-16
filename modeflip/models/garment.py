from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, Integer, List, Float


class Garment(Object):
	gid = Integer(nullable=False)
	cid = Integer(nullable=False)
	did = Integer(nullable=False)
	price = Float(nullable=False)
	description = String()
	shop_link = String()
	pictures = List(value=String())


class GarmentConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['garments']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1), ('cid', 1), ('gid', 1)])

	def get(self, did, cid, gid):
		doc = self.collection.find_one({'did': did, 'cid': cid, 'gid': gid}, {'_id': 0})
		return Garment(**doc) if doc else None

	def get_all_garments_by_designer_collection(self, did, cid):
		return [Garment(**doc) for doc in self.collection.find({'did': did, 'cid': cid}, {'_id': 0})]

	def set(self, garment):
		garment.validate()
		self.collection.update({'did': garment.did, 'cid': garment.cid, 'gid': garment.gid}, garment.__json__(), safe=True, upsert=True)
		return garment

	def delete(self, did, cid, gid):
		garment = self.get(did, cid, gid)
		if garment:
			self.collection.remove({'did': did, 'cid': cid, 'gid': gid})
			return True
		return False