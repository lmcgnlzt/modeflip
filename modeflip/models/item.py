#coding=utf-8
from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import Integer, Float

from modeflip.models.designer import Picture


class Item(Object):
	VALID_SIZES = ('XS', 'S', 'M', 'L', 'XL', 'F', 'F+')

	tag = String(nullable=False, mutator=lambda x: x.strip())
	name = String(nullable=False, mutator=lambda x: x.strip())
	original_price = Float(nullable=False)
	available_sizes = List(value=String(nullable=False, validator=lambda v: v in Item.VALID_SIZES)) #pylint: disable=E0602)

	# Merchant manually entered values for transactions
	size = String(validator=lambda v: v in Item.VALID_SIZES) #pylint: disable=E0602)
	price = Float(default=None)

	# Optional
	did = Integer()
	cid = Integer()
	shop_link = String()
	thumbnail = EmbeddedObject(Picture)

	@property
	def points(self):
		if self.price is not None:
			return round(self.price * 0.1)

	def __json__(self):
		json_self = Object.__json__(self)
		json_self['points'] = self.points
		return json_self


class ItemConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['items']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('tag', 1)], unique=True)

	def get_by_tag(self, tag):
		doc = self.collection.find_one({'tag': tag}, {'_id': 0})
		return Item(**doc) if doc else None

	def get_all_tags(self):
		return [str(c['tag']) for c in self.collection.find({}, {'_id':0, 'tag':1})]

	def set(self, item):
		item.validate()
		self.collection.update({'tag': item.tag}, item.__json__(), safe=True, upsert=True)
		return item

	def delete(self, tag):
		item = self.get_by_tag(tag)
		if item:
			self.collection.remove({'tag': tag})
			return True
		return False