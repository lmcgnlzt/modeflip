#coding=utf-8
from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import Integer, Float

from modeflip.models.designer import Picture


class Item(Object):
	VALID_SIZES = ('XS', 'S', 'M', 'L', 'XL', 'F', 'F+')

	CATS = ['上衣', '下装', '裙子', '配饰', '皮衣', '羽绒服']
	CAT_MAP = {
		'01': {'subcat':'连衣裙', 	'cat':'裙子'},
		'02': {'subcat':'半裙', 		'cat':'裙子'},
		'03': {'subcat':'上衣', 		'cat':'上衣'},
		'04': {'subcat':'T恤', 		'cat':'上衣'},
		'05': {'subcat':'毛衣', 		'cat':'上衣'},
		'06': {'subcat':'衬衫', 		'cat':'上衣'},
		'07': {'subcat':'西服', 		'cat':'上衣'},
		'08': {'subcat':'吊带', 		'cat':'上衣'},
		'09': {'subcat':'马甲', 		'cat':'上衣'},
		'10': {'subcat':'夹克', 		'cat':'上衣'},
		'11': {'subcat':'风衣', 		'cat':'上衣'},
		'12': {'subcat':'大衣', 		'cat':'上衣'},
		'13': {'subcat':'裤子', 		'cat':'下装'},
		'14': {'subcat':'短裤', 		'cat':'下装'},
		'15': {'subcat':'包', 		'cat':'配饰'},
		'16': {'subcat':'腰带', 		'cat':'配饰'},
		'17': {'subcat':'项链', 		'cat':'配饰'},
		'18': {'subcat':'手镯', 		'cat':'配饰'},
		'19': {'subcat':'戒指', 		'cat':'配饰'},
		'20': {'subcat':'羽绒服', 	'cat':'羽绒服'},
		'21': {'subcat':'毛织连衣裙','cat':'裙子'},
		'22': {'subcat':'毛织半裙', 	'cat':'裙子'},
		'23': {'subcat':'皮衣', 		'cat':'皮衣'},
		}

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

	@property
	def sub_cat(self):
		return self.CAT_MAP.get(self.tag[3:5], {}).get('subcat', 'unknown')

	@property
	def cat(self):
		return self.CAT_MAP.get(self.tag[3:5], {}).get('cat', 'unknown')

	def __json__(self):
		json_self = Object.__json__(self)
		json_self['points'] = self.points
		json_self['cat'] = self.cat
		json_self['sub_cat'] = self.sub_cat
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
		return [{'tag':c['tag'], 'name':c['name'].encode('utf-8')} for c in self.collection.find({}, {'_id':0, 'tag':1, 'name':1})]

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