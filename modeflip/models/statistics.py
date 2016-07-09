from modeflip.valid_model import Object
from modeflip.utils.valid_model_utils import Integer


class Statistics(Object):
	did = Integer()
	likes = Integer(default=0)
	wishes = Integer(default=0)


class StatisticsConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['statistics']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1)])

	def get(self, did):
		doc = self.collection.find_one({'did': did})
		return Statistics(**doc) if doc else None

	def set(self, stats):
		stats.validate()
		self.collection.update({'did': stats.did}, stats.__json__(), safe=True, upsert=True)
		return stats

	def get_likes(self, did):
		result = self.collection.find_one({'did': did}, {'likes': 1})
		return result['likes'] if result else None

	def do_like(self, did):
		curr_likes = self.get_likes(did)
		if curr_likes is not None:
			self.collection.update({'did': did}, {'$inc': {'likes': 1}})
			return curr_likes + 1

	def get_wishes(self, did):
		result = self.collection.find_one({'did': did}, {'wishes': 1})
		return result['wishes'] if result else None

	def do_wish(self, did):
		curr_wishes = self.get_wishes(did)
		if curr_wishes is not None:
			self.collection.update({'did': did}, {'$inc': {'wishes': 1}})
			return curr_wishes + 1

	def delete(self, did):
		stats = self.get(did)
		if stats:
			self.collection.remove({'did': did})
			return True
		return False