#coding=utf-8

from datetime import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *



local_config = get_configuration('production')
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)



############################################################################################################
DID = 2


bio = "Eillen, 1954年，圣.洛朗参加国际羊毛局举办的设计大奖赛，以一套黑色鸡尾酒会服荣获女装一等奖，以此为契机进入迪奥尔店的主任设计师。60年代的后半期，圣.洛朗使自己的高级时装和高级成衣遍及全世界，1971年春他推出沙漏形的40年代风格，掀起一阵回归潮, 1974年秋他发表哥萨克风格，引起民族风格服装的流行。直到现在，他仍是巴黎时装界举足轻重的一位设计师。"


profile_images = ProfileImages(
		icon_url='http://assets.modeflip.com/eileen/icon/icon.jpg',
		image_url='http://assets.modeflip.com/eileen/icon/image.jpg',
		background_url='http://assets.modeflip.com/eileen/icon/background.jpg',
	)


experience_content = ExperienceContent(
	brands=[
		'http://assets.modeflip.com/eileen/experience/brand/maxmara.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/cerruti.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/dkny.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/gianni.jpg',
		],
	pic_title='',
	pics = [
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/1s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/1.jpg', title='1'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/2s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/2.jpg', title='2'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/3s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/3.jpg', title='3'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/4s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/4.jpg', title='4'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/5s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/5.jpg', title='5'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/6s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/6.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/7s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/7.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/8s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/8.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/9s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/9.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/10s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/10.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/11s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/11.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/12s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/12.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/13s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/13.jpg'),
		Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/14s.jpg', image='http://assets.modeflip.com/eileen/experience/pics/14.jpg'),
	],

	# video_title='Burberry 2016',
	# videos=['images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4'],
	)


exclusive_content = ExclusiveContent(
	title='Max Mara',
	pics=[
		'http://assets.modeflip.com/eileen/exclusive/pics/1.jpg',
		'http://assets.modeflip.com/eileen/exclusive/pics/2.jpg',
		'http://assets.modeflip.com/eileen/exclusive/pics/3.jpg',
		],
	videos=[
		Video(
				thumbnail='http://assets.modeflip.com/eileen/exclusive/videos/thumbnail.jpg',
				poster='http://assets.modeflip.com/eileen/exclusive/videos/thumbnail.png',
				url='http://assets.modeflip.com/eileen/exclusive/videos/MaxMara.mp4',
			)
		]
	)



signatrue_products = [
	SignatrueProduct(
			picture='http://assets.modeflip.com/eileen/product/1.jpg',
			title='设计师环保活页笔记本夹',
			subtitle='标志产品',
			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
			shop_link='http://notebook_shop_link',
		),
	SignatrueProduct(
			picture='http://assets.modeflip.com/eileen/product/2.jpg',
			title='A5 设计师独家设计卡',
			# subtitle='Signature Product',
			# desc='This is an awesome notebook, you will love it',
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


d = Designer(
		did=DID,
		name='Eileen',
		profile_images=profile_images,
		is_active=True,
		origin='New York',
		bio=bio,
		experience_content=experience_content,
		exclusive_content=exclusive_content,
		signatrue_products=signatrue_products,
		private_musics=private_musics,
		)


dc.set(d)

print 'designer info saved'



############################################################################################################
CID_2 = 2
CID_1 = 1


c_july = Collection(
		cid=CID_2,
		did=DID,
		title='七月限量主题春夏系列',
		released=datetime(2016, 7, 15),
		signatrue_pics=[
			'http://assets.modeflip.com/eileen/collections/201607/signature/pics/1.jpg',
			'http://assets.modeflip.com/eileen/collections/201607/signature/pics/2.jpg',
		],
		signatrue_videos=[
			Video(
				thumbnail='http://assets.modeflip.com/eileen/collections/201607/signature/videos/thumbnail.jpg',
				poster='http://assets.modeflip.com/eileen/collections/201607/signature/videos/thumbnail.png',
				url='http://assets.modeflip.com/eileen/collections/201607/signature/videos/MaxMara.mp4',
			)
		],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=True,
		)


c_june = Collection(
		cid=CID_1,
		did=DID,
		title='六月限量主题春夏系列',
		released=datetime(2016, 6, 15),
		# signatrue_pics=[
		# 	'http://assets.modeflip.com/eileen/images/modeflip/collections/june/signature/1.jpg',
		# 	'http://assets.modeflip.com/eileen/images/modeflip/collections/june/signature/2.jpg',
		# ],
		# signatrue_videos=[
		# 	'images/modeflip/MaxMara_Spring_Summer_2011_MilanHD2.mp4',
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=False,
		)



collections = [
	c_july,
	c_june,
]

[cc.set(c) for c in collections]
print 'collection info saved'




############################################################################################################


g_july_1 = Garment(
				gid=1,
				cid=CID_2,
				did=DID,
				price=888,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_july_2 = Garment(
				gid=2,
				cid=CID_2,
				did=DID,
				price=888,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/details/2.jpg'),
						]
				)



g_june_1 = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_june_2 = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/eileen/collections/201607/garments/2/details/2.jpg'),
						]
				)



garments = [
	g_july_1,
	g_july_2,
	g_june_1,
	g_june_2,
]

[gc.set(g) for g in garments]
print 'garments info saved'