from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, Bool, List, EmbeddedObject
from modeflip.utils.valid_model_utils import Integer, DateTime, Float

from modeflip.models.common import ProfileImages, Picture, Video, Music, PicturePage
from modeflip.models.collection import Collection
from modeflip.models.statistics import Statistics


class ExperienceContent(Object):
	brands = List(value=String(), validator=lambda x: all('/' in i for i in x))
	thumbnails = List(value=String(), validator=lambda x: all('/' in i for i in x))
	pics = List(value=EmbeddedObject(Picture)) # all pictures


class ExclusiveContent(Object):
	title = String()
	pics = List(value=String(), validator=lambda x: all('/' in i for i in x))
	videos = List(value=EmbeddedObject(Video))


class PreMarketContent(Object):
	target_date = String()
	target_pic = String(validator=lambda x: '/' in x)


class PrivateMusic(Object):
	music_icon = String()
	title = String()
	author = String()
	link = String(validator=lambda x: '/' in x)


class SignatrueProduct(Object):
	picture = String(validator=lambda x: '/' in x)
	title = String()
	subtitle = String()
	desc = String()
	shop_link = String(validator=lambda x: '/' in x)


class Designer(Object):
	did = Integer(nullable=False)
	name = String(nullable=False, validator=lambda x: x and len(x) >0)
	profile_images = EmbeddedObject(ProfileImages)
	is_active = Bool(default=False)
	on_market = Bool(default=True)
	origin = String(mutator=lambda x: x.strip().upper())
	intro = String()
	bio = String()
	experience_content = EmbeddedObject(ExperienceContent)
	exclusive_content = EmbeddedObject(ExclusiveContent)
	pre_mkt_content = EmbeddedObject(PreMarketContent)
	likes_and_wishes = EmbeddedObject(Statistics)


	signatrue_products = List(value=EmbeddedObject(SignatrueProduct))
	private_musics = List(value=EmbeddedObject(PrivateMusic))

	collections = List(value=EmbeddedObject(Collection)) # place holder for data transformation


class DesignerConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['designers']
		self.ensure_indexes()

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1)])
		self.collection.ensure_index([('name', 1)])

	def get(self, did):
		doc = self.collection.find_one({'did': did})
		return Designer(**doc) if doc else None

	def get_next_designer(self, curr_did):
		res = list(self.collection.find({'did': {'$gt': curr_did}}, sort=[('did', 1)], limit=2))
		if res:
			d = Designer(**res[0])
			has_next = len(res) > 1
			return d, has_next
		else:
			return None, False

	def get_all_ids(self):
		return [c['did'] for c in self.collection.find({}, {'_id':0, 'did':1}).sort('did', 1)]

	def get_all_designers(self):
		return [Designer(**doc) for doc in self.collection.find({}).sort('did', 1)]

	def get_designers_by_page(self, _page=1, _perPage=10):
		return [Designer(**doc) for doc in self.collection.find({'did': {'$gt': (_page-1)*_perPage, '$lte': _page*_perPage}}, {'_id': 0}).sort('name', 1)]

	def set(self, designer):
		designer.validate()
		self.collection.update({'did': designer.did}, designer.__json__(), safe=True, upsert=True)
		return designer

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
 - new_arrival


Garment
 - gid
 - cid
 - did
 - price
 - description
 - pictures



Refined Model
 - did
 - name
 - icon_url
 - background_url
 - is_active
 - origin
 - likes
 - subscribers
 - bio
 - experience_content
 	- former_brands (urls)
 	- former_pic_title
 	- former_pics (urls)
 	- former_video_title
 	- former_videos (urls)
 - exclusive_content
 	- exclusive_content_title
 	- exclusive_pics (urls)
 - collections (sort by month)
 	- cid
 	- did
 	- c_title
 	- release_date
 	- signatrue_pics (urls)
 	- signatrue_videos (urls)
 	- signatrue_musics (urls)
	- garments
		- gid
		- cid
		- did
		- shop_link
		- pictures (urls)
 - product_pics (urls) [static info???]
 - private_musics
 	- music_icon
 	- title
 	- author
 	- link



"""