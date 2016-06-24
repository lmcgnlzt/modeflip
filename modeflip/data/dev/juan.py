#coding=utf-8

# from pprint import pprint
import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)


dc = DesignerConfig(get_database('mf_config'))


profile_images = ProfileImages(
	icon_url='images/resources/juan/icon/icon.jpg',
	image_url='images/resources/juan/icon/image.jpg',
	background_url='images/resources/juan/icon/background.jpg',
	)

experience_content = ExperienceContent(
	brands=[
		'images/resources/juan/experience/brand/maxmara.jpg',
		'images/resources/juan/experience/brand/cerruti.jpg',
		'images/resources/juan/experience/brand/dkny.jpg',
		'images/resources/juan/experience/brand/gianni.jpg',
		],
	pic_title='',
	pages = [
		PicturePage(
			pics = [
				Picture(thumbnail='images/resources/juan/experience/pics/1s.jpg', image='images/resources/juan/experience/pics/1.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/2s.jpg', image='images/resources/juan/experience/pics/2.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/3s.jpg', image='images/resources/juan/experience/pics/3.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/4s.jpg', image='images/resources/juan/experience/pics/4.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/5s.jpg', image='images/resources/juan/experience/pics/5.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/6s.jpg', image='images/resources/juan/experience/pics/6.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/7s.jpg', image='images/resources/juan/experience/pics/7.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/8s.jpg', image='images/resources/juan/experience/pics/8.jpg'),
			]
		),
		PicturePage(
			pics = [
				Picture(thumbnail='images/resources/juan/experience/pics/11s.jpg', image='images/resources/juan/experience/pics/11.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/12s.jpg', image='images/resources/juan/experience/pics/12.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/13s.jpg', image='images/resources/juan/experience/pics/13.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/14s.jpg', image='images/resources/juan/experience/pics/14.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/5s.jpg', image='images/resources/juan/experience/pics/5.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/6s.jpg', image='images/resources/juan/experience/pics/6.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/7s.jpg', image='images/resources/juan/experience/pics/7.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/8s.jpg', image='images/resources/juan/experience/pics/8.jpg'),
			]
		),
		PicturePage(
			pics = [
				Picture(thumbnail='images/resources/juan/experience/pics/1s.jpg', image='images/resources/juan/experience/pics/1.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/2s.jpg', image='images/resources/juan/experience/pics/2.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/12s.jpg', image='images/resources/juan/experience/pics/12.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/13s.jpg', image='images/resources/juan/experience/pics/13.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/14s.jpg', image='images/resources/juan/experience/pics/14.jpg'),
				Picture(thumbnail='images/resources/juan/experience/pics/5s.jpg', image='images/resources/juan/experience/pics/5.jpg'),
				# Picture(thumbnail='images/resources/juan/images/pics/7s.jpg', image='images/resources/juan/images/pics/7.jpg'),
				# Picture(thumbnail='images/resources/juan/images/pics/8s.jpg', image='images/resources/juan/images/pics/8.jpg'),
			]
		)
	],
	# video_title='Burberry 2016',
	# videos=['images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4'],
	)


exclusive_content = ExclusiveContent(
	title='Max Mara',
	pics=[
		'images/resources/juan/exclusive/pics/1.jpg',
		'images/resources/juan/exclusive/pics/2.jpg',
		'images/resources/juan/exclusive/pics/3.jpg',
		],
	videos=[
		Video(
				thumbnail='images/resources/juan/exclusive/videos/thumbnail.jpg',
				url='images/resources/juan/exclusive/videos/MaxMara.mp4',
			)
		]
	)


garments_july = [
	Garment(
		gid=1,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/resources/juan/collections/201607/garments/1/pre1s.jpg',
			image='images/resources/juan/collections/201607/garments/1/pre1.jpg',
			title='蕾丝花边裙',
			),
		more_pics = [
			Picture(title="细节1", image='images/resources/juan/collections/201607/garments/1/details/1.jpg'),
			Picture(title="细节2", image='images/resources/juan/collections/201607/garments/1/details/2.jpg'),
			Picture(title="细节3", image='images/resources/juan/collections/201607/garments/1/details/3.jpg'),
			Picture(title="细节4", image='images/resources/juan/collections/201607/garments/1/details/4.jpg'),
			]
		),
	Garment(
		gid=2,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/resources/juan/collections/201607/garments/2/new1s.jpg',
			image='images/resources/juan/collections/201607/garments/2/1s.jpg',
			title='无袖开衩长裙',
			),
		more_pics = [
			Picture(title="细节1", image='images/resources/juan/collections/201607/garments/2/details/1.jpg'),
			Picture(title="细节2", image='images/resources/juan/collections/201607/garments/2/details/2.jpg'),
			]
		),
	]

garments_june = [
	Garment(
		gid=1,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/resources/juan/collections/201606/garments/1/pre1s.jpg',
			image='images/resources/juan/collections/201606/garments/1/pre1.jpg',
			title='复古开叉长裙',
			),
		more_pics = [
			Picture(title="细节1", image='images/resources/juan/collections/201606/garments/1/details/1.jpg'),
			Picture(title="细节2", image='images/resources/juan/collections/201606/garments/1/details/2.jpg'),
			Picture(title="细节3", image='images/resources/juan/collections/201606/garments/1/details/3.jpg'),
			Picture(title="细节4", image='images/resources/juan/collections/201606/garments/1/details/4.jpg'),
			]
		),
	Garment(
		gid=2,
		shop_link='http://shop_link',
		pic = Picture(
			thumbnail='images/resources/juan/collections/201606/garments/2/new1s.jpg',
			image='images/resources/juan/collections/201606/garments/2/1s.jpg',
			title='镂空两件套裙',
			),
		more_pics = [
			Picture(title="细节1", image='images/resources/juan/collections/201606/garments/2/details/1.jpg'),
			Picture(title="细节2", image='images/resources/juan/collections/201606/garments/2/details/2.jpg'),
			]
		),
	]

collections = [
	Collection(
		cid=2,
		title='七月限量主题春夏系列',
		released=datetime.datetime(2016, 7, 15),
		signatrue_pics=[
			'images/resources/juan/collections/201607/signature/pics/1.jpg',
			'images/resources/juan/collections/201607/signature/pics/2.jpg',
		],
		signatrue_videos=[
			Video(
				thumbnail='images/resources/juan/collections/201607/signature/videos/thumbnail.jpg',
				url='images/resources/juan/collections/201607/signature/videos/MaxMara.mp4',
			)
		],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		garments=garments_july,
		new_arrival=True,
		),

	Collection(
		cid=1,
		title='六月限量主题春夏系列',
		released=datetime.datetime(2016, 6, 15),
		# signatrue_pics=[
		# 	'images/resources/juan/images/modeflip/collections/june/signature/1.jpg',
		# 	'images/resources/juan/images/modeflip/collections/june/signature/2.jpg',
		# ],
		# signatrue_videos=[
		# 	'images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4',
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		garments=garments_june,
		new_arrival=False,
		),
	]



signatrue_products = [
	SignatrueProduct(
			picture='images/resources/juan/product/1.jpg',
			title='designer notebook',
			subtitle='Signature Product',
			desc='This is an awesome notebook, you will love it',
			shop_link='http://notebook_shop_link',
		),
	SignatrueProduct(
			picture='images/resources/juan/product/2.jpg',
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


# bio1 = "Juan was born April 9, 1963 in New York City. Marc's life was completely altered following the death of his father at the age of 7. He would eventually move in with his grandmother and that made all the difference. Marc entered the Parsons School of Design and later a position at Perry Ellis. Jacobs started his own label and continued to impress the fashion world"
bio1 = "巴黎高级时装设计师，出生于啊尔及利亚。1954年，圣.洛朗参加国际羊毛局举办的设计大奖赛，以一套黑色鸡尾酒会服荣获女装一等奖，以此为契机进入迪奥尔店的主任设计师。60年代的后半期，圣.洛朗使自己的高级时装和高级成衣遍及全世界，1971年春他推出沙漏形的40年代风格，掀起一阵回归潮, 1974年秋他发表哥萨克风格，引起民族风格服装的流行。直到现在，他仍是巴黎时装界举足轻重的一位设计师。"

d = Designer(
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


dc.set(d)

print 'Done'