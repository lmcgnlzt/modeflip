#coding=utf-8
from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject
from modeflip.utils.valid_model_utils import Integer, Float

from modeflip.models.designer import Picture


class Item(Object):
	VALID_SIZES = ('XS', 'S', 'M', 'L', 'XL', 'F', 'F+')

	CATS = ['上衣', '下装', '裙子', '配饰', '皮衣', '羽绒服']
	CAT_MAP = {
		'01': {'cat':'裙子', 		'subcat':'连衣裙'},
		'02': {'cat':'裙子', 		'subcat':'半裙'},
		'03': {'cat':'上装', 		'subcat':'上衣'},
		'04': {'cat':'上装', 		'subcat':'T恤'},
		'05': {'cat':'上装', 		'subcat':'毛衣'},
		'06': {'cat':'上装', 		'subcat':'衬衫'},
		'07': {'cat':'外套', 		'subcat':'西服'},
		'08': {'cat':'上装', 		'subcat':'吊带'},
		'09': {'cat':'上装', 		'subcat':'马甲'},
		'10': {'cat':'外套',  		'subcat':'夹克'},
		'11': {'cat':'外套', 		'subcat':'风衣'},
		'12': {'cat':'外套', 		'subcat':'大衣'},
		'13': {'cat':'下装', 		'subcat':'裤子'},
		'14': {'cat':'下装', 		'subcat':'短裤'},
		'15': {'cat':'配饰', 		'subcat':'包'},
		'16': {'cat':'配饰', 		'subcat':'腰带'},
		'17': {'cat':'配饰', 		'subcat':'项链'},
		'18': {'cat':'配饰', 		'subcat':'手镯'},
		'19': {'cat':'配饰', 		'subcat':'戒指'},
		'20': {'cat':'外套', 		'subcat':'羽绒服'},
		'21': {'cat':'裙子', 		'subcat':'毛织连衣裙'},
		'22': {'cat':'裙子', 		'subcat':'毛织半裙'},
		'23': {'cat':'外套', 		'subcat':'皮衣'},
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