from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, Bool, List, EmbeddedObject
from modeflip.utils.valid_model_utils import Integer, DateTime


class ProfileImages(Object):
	icon_url = String(validator=lambda x: '/' in x)
	image_url = String(validator=lambda x: '/' in x)
	background_url = String(validator=lambda x: '/' in x)


class Picture(Object):
	title = String()
	thumbnail = String(validator=lambda x: '/' in x)
	image = String(validator=lambda x: '/' in x)


class Video(Object):
	title = String()
	thumbnail = String(validator=lambda x: '/' in x)
	url = String(validator=lambda x: '/' in x)


class Music(Object):
	title = String()
	thumbnail = String(validator=lambda x: '/' in x)
	url = String(validator=lambda x: '/' in x)


class PicturePage(Object):
	pics = List(value=EmbeddedObject(Picture))


class ExperienceContent(Object):
	brands = List(value=String(), validator=lambda x: all('/' in i for i in x))
	pic_title = String()
	# pics = List(value=EmbeddedObject(Picture))
	pages = List(value=EmbeddedObject(PicturePage))
	# pics = List(value=List(value=EmbeddedObject(Picture)))
	video_title = String()
	videos = List(value=String(), validator=lambda x: all('/' in i for i in x))


class ExclusiveContent(Object):
	title = String()
	pics = List(value=String(), validator=lambda x: all('/' in i for i in x))
	videos = List(value=EmbeddedObject(Video))


class Garment(Object):
	gid = Integer(nullable=False)
	shop_link = String()
	pic = EmbeddedObject(Picture)
	more_pics = List(value=EmbeddedObject(Picture))


class Collection(Object):
	cid = Integer(nullable=False)
	title = String()
	released = DateTime(nullable=False)
	signatrue_pics = List(value=String(), validator=lambda x: all('/' in i for i in x))
	signatrue_videos = List(value=EmbeddedObject(Video))
	signatrue_musics = List(value=EmbeddedObject(Music))
	garments = List(value=EmbeddedObject(Garment))
	new_arrival = Bool(default=False)


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
	origin = String(mutator=lambda x: x.strip().upper())
	likes = Integer(default=0)
	subscribers = Integer(default=0)
	bio = String()
	experience_content = EmbeddedObject(ExperienceContent)
	exclusive_content = EmbeddedObject(ExclusiveContent)
	collections = List(value=EmbeddedObject(Collection))

	signatrue_products = List(value=EmbeddedObject(SignatrueProduct))
	private_musics = List(value=EmbeddedObject(PrivateMusic))


class DesignerConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['designers']

	def ensure_indexes(self):
		self.collection.ensure_index([('did', 1)])
		self.collection.ensure_index([('name', 1)])
		self.ensure_indexes()

	def get(self, did):
		doc = self.collection.find_one({'did': did})
		return Designer(**doc) if doc else None

	def get_all_ids(self):
		return [c['did'] for c in self.collection.find({}, {'_id':0, 'did':1}).sort('did', 1)]

	def get_all_designers(self):
		return [Designer(**doc) for doc in self.collection.find({}).sort('name', 1)]

	def get_designers_by_page(self, _page=1, _perPage=10):
		return [Designer(**doc) for doc in self.collection.find({'did': {'$gt': (_page-1)*_perPage, '$lte': _page*_perPage}}, {'_id': 0}).sort('name', 1)]

	def set(self, designer):
		designer.validate()
		self.collection.update({'did': designer.did}, designer.__json__(), safe=True, upsert=True)
		return designer

	def get_likes(self, did):
		result = self.collection.find_one({'did': did}, {'likes': 1})
		return result['likes'] if result else None

	def do_like(self, did):
		curr_likes = self.get_likes(did)
		if curr_likes is not None:
			self.collection.update({'did': did}, {'$inc': {'likes': 1}})
			return curr_likes + 1

	def get_subscribes(self, did):
		result = self.collection.find_one({'did': did}, {'subscribers': 1})
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