from datetime import datetime

from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import DateTime, Integer

from modeflip.models.transaction import Transaction


class Member(Object):
	open_id = String(mutator=lambda x: x.strip(), nullable=False) # wechat open_id
	created_on = DateTime(default=datetime.utcnow())
	last_updated_on = DateTime(default=datetime.utcnow())
	shopping_history = List(value=EmbeddedObject(Transaction)) # this is okay since history not growing too fast

	@property
	def total_points(self):
		return sum([sum([i.points for i in history.items]) for history in self.shopping_history]) # calc total points on the fly

	def __json__(self):
		json_self = Object.__json__(self)
		json_self['total_points'] = self.total_points
		return json_self


class MemberConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['members']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('open_id', 1)], unique=True)

	def get(self, open_id):
		doc = self.collection.find_one({'open_id': open_id}, {'_id': 0})
		return Member(**doc) if doc else None

	def set(self, member):
		member.validate()
		self.collection.update({'open_id': member.open_id}, member.__json__(), safe=True, upsert=True)
		return member

	def delete(self, open_id):
		member = self.get(open_id)
		if member:
			self.collection.remove({'open_id': open_id})
			return True
		return False