from datetime import datetime

from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import DateTime, Integer, Float

from modeflip.models.item import Item
from modeflip.models.common import Video, Music


class Transaction(Object):
	tid = Integer(nullable=False)
	merchant_name = String(mutator=lambda x: x.strip(), nullable=False) # user_name of Merchant
	open_id = String(mutator=lambda x: x.strip()) # open_id of member
	gift = String(mutator=lambda x: x.strip())
	trans_date = DateTime(datetime.utcnow())
	items = List(value=EmbeddedObject(Item))



class TransactionConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['transactions']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('tid', 1)], unique=True)
		self.collection.ensure_index([('merchant_name', 1), ('trans_date', -1)])
		# self.collection.ensure_index([('open_id', 1), ('trans_date', -1)])

	def get_next_available_id(self):
		try:
			return list(self.collection.find({}, {'tid': 1}, sort=[('tid', -1)], limit=1))[0]['tid'] + 1
		except IndexError:
			return 1

	def get(self, tid):
		doc = self.collection.find_one({'tid': tid}, {'_id': 0})
		return Transaction(**doc) if doc else None

	def get_all_ids(self):
		return [c['tid'] for c in self.collection.find({}, {'_id':0, 'tid':1}).sort('tid', 1)]

	def get_by_merchant_name(self, merchant_name):
		return [Transaction(**doc) for doc in self.collection.find({'merchant_name': merchant_name}, {'_id': 0}).sort('trans_date', -1)]

	# def get_by_open_id(self, open_id):
	# 	return [Transaction(**doc) for doc in self.collection.find({'open_id': open_id}, {'_id': 0}).sort('trans_date', -1)]

	def get_all_by_merchant_name_within(self, merchant_name, start_date, end_date):
		return [Transaction(**doc) for doc in self.collection.find({'merchant_name': merchant_name, 'trans_date': {'$gte': start_date, '$lt': end_date}}, {'_id': 0})]

	# def get_all_by_open_id_within(self, open_id, start_date, end_date):
	# 	return [Transaction(**doc) for doc in self.collection.find({'open_id': open_id, 'trans_date': {'$gte': start_date, '$lt': end_date}}, {'_id': 0})]

	def set(self, transaction):
		transaction.validate()
		self.collection.update({'tid': transaction.tid}, transaction.__json__(), safe=True, upsert=True)
		return transaction

	def delete(self, tid):
		transaction = self.get(tid)
		if transaction:
			self.collection.remove({'tid': tid})
			return True
		return False