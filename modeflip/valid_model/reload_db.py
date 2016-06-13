# from pprint import pprint
import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)


dc = DesignerConfig(get_database('mf_config'))


profile_images = ProfileImages(
	icon_url='http://icon_url.com',
	image_url='http://image_url.com',
	background_url='http://background_url.com',
	)

experience_content = ExperienceContent(
	brands=['http://brand_1.com', 'http://brand_2.com'],
	pic_title='',
	pics = [
		Picture(thumbnail='http://thumbnail_1.com', image='http://image_1.com'),
		Picture(thumbnail='http://thumbnail_2.com', image='http://image_2.com'),
		],
	video_title='Burberry 2016',
	videos=['http://video_1.com', 'http://video_2.com'],
	)


exclusive_content = ExclusiveContent(
	title='Max Mara',
	pics=['http://pic_1.com', 'http://pic_2.com'],
	)


garments = [
	Garment(
		shop_link='http://shop_link',
		pics = [
			Picture(thumbnail='http://garment_thumbnail_1.com', image='http://garment_image_1.com'),
			Picture(thumbnail='http://garment_thumbnail_2.com', image='http://garment_image_2.com'),
			]
		)
	]

collections = [
	Collection(
		title='07/2016 SPRING-SUMMER COLLECTIONS',
		released=datetime.datetime(2016, 8, 15),
		signatrue_pics=[
			'http://sig_pic_1.com',
			'http://sig_pic_2.com',
		],
		signatrue_videos=[
			'http://sig_video_1.com',
			'http://sig_video_2.com',
		],
		signatrue_musics=[
			'http://sig_music_1.com',
			'http://sig_music_2.com',
		],
		garments=garments,
		new_arrival=True,
		),
	]



signatrue_products = [
	SignatrueProduct(
			picture='http://sig_product_1',
			title='designer notebook',
			subtitle='Signature Product',
			desc='This is an awesome notebook, you will love it',
			shop_link='http://notebook_shop_link',
		),
	]


private_musics = [
	PrivateMusic(
		music_icon='http://music_icon_1.com',
		title='Ugly Is Beautiful',
		author='David Usher',
		link='http://private_music_1.com'
		),
	PrivateMusic(
		music_icon='http://music_icon_2.com',
		title='Beautiful Is Ugly',
		author='Usher David',
		link='http://private_music_2.com'
		),
	]


bio1 = "Sophia Tezel was born April 9, 1963 in New York City. Marc's life was completely altered following the death of his father at the age of 7. He would eventually move in with his grandmother and that made all the difference. Marc entered the Parsons School of Design and later a position at Perry Ellis. Jacobs started his own label and continued to impress the fashion world"
d1 = Designer(
		did=1,
		name='Sophia Tezel',
		profile_images=profile_images,
		is_active=True,
		origin='NEW YORK',
		likes=0,
		subscribers=0,
		bio=bio1,
		experience_content=experience_content,
		exclusive_content=exclusive_content,
		collections=collections,
		signatrue_products=signatrue_products,
		private_musics=private_musics,
		)


d_list = [d1]


[dc.set(d) for d in d_list]

print 'Done'