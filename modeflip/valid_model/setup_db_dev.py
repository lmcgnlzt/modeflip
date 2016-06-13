# from pprint import pprint
import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)


dc = DesignerConfig(get_database('mf_config'))


profile_images = ProfileImages(
	# icon_url='file:///Users/mli/modepages/tinybar/code/images/modeflip/icon/touxiang.jpg',
	icon_url='file:///Users/mli/modepages/tinybar/code/images/pictures/3s.jpg',
	image_url='file:///Users/mli/modepages/tinybar/code/images/home/eileen_new_york.png',
	background_url='file:///Users/mli/modepages/tinybar/code/images/modeflip/icon/background.jpg',
	)

experience_content = ExperienceContent(
	brands=[
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/brand/maxmara.jpg',
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/brand/cerruti.jpg',
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/brand/dkny.jpg',
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/brand/cerruti.jpg',
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/brand/gianni.jpg',
		],
	pic_title='',
	pages = [
		PicturePage(
			pics = [
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/1s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/1.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/2s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/2.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/3s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/3.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/4s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/4.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/6s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/6.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8.jpg'),
			]
		),
		PicturePage(
			pics = [
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/11s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/11.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/12s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/12.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/13s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/13.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/14s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/14.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/6s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/6.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8.jpg'),
			]
		),
		PicturePage(
			pics = [
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/1s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/1.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/2s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/2.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/12s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/12.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/13s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/13.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/14s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/14.jpg'),
				Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/5.jpg'),
				# Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/7.jpg'),
				# Picture(thumbnail='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8s.jpg', image='file:///Users/mli/modepages/tinybar/code/images/modeflip/history/8.jpg'),
			]
		)
	],
	video_title='Burberry 2016',
	videos=['images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4'],
	)


exclusive_content = ExclusiveContent(
	title='Max Mara',
	pics=[
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/1.jpg',
		'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/2.jpg'
		],
	videos=[
		Video(
				thumbnail='images/thumbnail.jpg',
				url='images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4',
			)
		]
	)


garments_august = [
	Garment(
		gid=1,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/modeflip/collections/june/garments/pre1s.jpg',
			image='images/home/detail1.png',
			title='Dress',
			),
		more_pics = [
			Picture(title="detail2", image='images/home/detail2.png'),
			Picture(title="detail3", image='images/home/detail3.png'),
			Picture(title="detail4", image='images/home/detail4.png'),
			Picture(title="detail5", image='images/home/detail5.png'),
			]
		),
	Garment(
		gid=2,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/modeflip/collections/june/garments/new1s.jpg',
			image='images/modeflip/collections/june/garments/pre1.jpg',
			title='Suit',
			),
		more_pics = [
			Picture(title="detail2", image='images/modeflip/collections/june/garments/pre1.jpg'),
			Picture(title="detail3", image='images/modeflip/collections/june/garments/pre1.jpg'),
			Picture(title="detail4", image='images/modeflip/collections/june/garments/pre1.jpg'),
			]
		)
	]

garments_july = [
	Garment(
		gid=1,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/modeflip/collections/june/garments/pre1s.jpg',
			image='images/home/detail1.png',
			title='Dress',
			),
		more_pics = [
			Picture(title="detail2", image='images/home/detail2.png'),
			Picture(title="detail3", image='images/home/detail3.png'),
			Picture(title="detail4", image='images/home/detail4.png'),
			Picture(title="detail5", image='images/home/detail5.png'),
			]
		),
	Garment(
		gid=2,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/modeflip/collections/june/garments/new1s.jpg',
			image='images/modeflip/collections/june/garments/pre1.jpg',
			title='Suit',
			),
		more_pics = [
			Picture(title="detail2", image='images/modeflip/collections/june/garments/pre1.jpg'),
			Picture(title="detail3", image='images/modeflip/collections/june/garments/pre1.jpg'),
			Picture(title="detail4", image='images/modeflip/collections/june/garments/pre1.jpg'),
			]
		)
	]

collections = [
	Collection(
		cid=2,
		title='08/2016 SPRING-SUMMER COLLECTIONS',
		released=datetime.datetime(2016, 8, 15),
		signatrue_pics=[
			'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/1.jpg',
			'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/2.jpg',
		],
		signatrue_videos=[
			Video(
				thumbnail='images/thumbnail.jpg',
				url='images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4',
			)
		],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		garments=garments_august,
		new_arrival=True,
		),

	Collection(
		cid=1,
		title='07/2016 SPRING-SUMMER COLLECTIONS',
		released=datetime.datetime(2016, 7, 15),
		# signatrue_pics=[
		# 	'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/1.jpg',
		# 	'file:///Users/mli/modepages/tinybar/code/images/modeflip/collections/june/signature/2.jpg',
		# ],
		# signatrue_videos=[
		# 	'images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4',
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		garments=garments_july,
		new_arrival=False,
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


bio1 = "Juan was born April 9, 1963 in New York City. Marc's life was completely altered following the death of his father at the age of 7. He would eventually move in with his grandmother and that made all the difference. Marc entered the Parsons School of Design and later a position at Perry Ellis. Jacobs started his own label and continued to impress the fashion world"
d1 = Designer(
		# did=1,
		# name='Sophia',
		# did=2,
		# name='Eileen',
		# did=3,
		# name='Gianni',
		did=4,
		name='Juan',
		profile_images=profile_images,
		is_active=True,
		origin='Mexico',
		likes=108,
		subscribers=16,
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