#coding=utf-8

import os.path
import random

from datetime import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)



############################################################################################################
DID = 2


intro = "来自纽约，Ralph Lauren全球设计副总裁22年，和Ralph先生一起建立起Ralph Lauren时尚帝国，同时被大名鼎鼎的唐纳川普（Donald John Trump）的女儿伊万卡川普 (Ivanka Trump)钦点，为其同名时尚品牌伊凡卡川普担任创意总监。目前担任着FIT时尚设计学院的客座讲师，是美国具有重要地位的设计师。"
bio = """Eileen Sullivan，来自纽约，任Ralph Lauren全球设计副总裁22年，与Ralph先生一起建立起Ralph Lauren时尚帝国。

|Eileen在巴黎和伦敦长大，从时尚设计专业毕业后，便被美国最经典奢侈品Ralph Lauren钦点，随后作为Ralph先生的左膀右臂任命全球设计副总裁。

|在22年中，Eileen重新定义了RL品牌的美国休闲服装风格，在她的设计管理下，Ralph Lauren在全球范围内开创了Polo Ralph Lauren的顶级经典的系列，包括RL蓝标、童装、运动、内衣、泳装、高尔夫等等。

|Eileen同时被大名鼎鼎的唐纳川普(Donald Trump) 的女儿伊凡卡川普 (Ivanka Trump) 钦点，为其同名时尚品牌伊凡卡川普担任创意总监。

|Eileen现在住在美国东岸的玛莎葡萄园岛，带来她自有品牌，Love for Edie及SquibeeS，同时担任着FIT时尚设计学院的客座讲师，是美国具有重要地位的设计师。
"""

profile_images = ProfileImages(
		icon_url='images/resources/eileen/icon/icon.jpg',
		image_url='images/resources/eileen/icon/image.jpg',
		background_url='images/resources/eileen/icon/background.jpg',
	)

pics = [Picture(thumbnail='images/resources/eileen/experience/pics/{}s.jpg'.format(i), image='images/resources/eileen/experience/pics/{}.jpg'.format(i)) for i in range(0, 74) if os.path.isfile('/Users/mli/modeapp/modeapp/static/images/resources/eileen/experience/pics/{}s.jpg'.format(i))]

sig_pics_ids = [1, 14, 3, 13, 5, 4, 15, 16, 17, 18, 19, 20, 21, 22, 23, 52]
sig_pics = [Picture(thumbnail='images/resources/eileen/experience/pics/{}s.jpg'.format(i), image='images/resources/eileen/experience/pics/{}.jpg'.format(i)) for i in sig_pics_ids if os.path.isfile('/Users/mli/modeapp/modeapp/static/images/resources/eileen/experience/pics/{}s.jpg'.format(i))]


experience_content = ExperienceContent(
	brands=[
		'images/resources/eileen/experience/brand/rl.jpg',
		'images/resources/eileen/experience/brand/eide.jpg',
		'images/resources/eileen/experience/brand/squibees.jpg',
		'images/resources/eileen/experience/brand/trump.jpg',
		],
	sig_pics = sig_pics,
	pics = pics,
	videos=[
		Video(
				thumbnail='images/resources/eileen/experience/videos/thumbnail.png',
				poster='images/resources/eileen/experience/videos/thumbnail.jpg',
				url='images/resources/eileen/experience/videos/MaxMara.mp4',
			)
		]
	)


exclusive_content = ExclusiveContent(
	title='独家签约 -- Exclusive Collections',
	pics=[
		'images/resources/eileen/exclusive/pics/1.jpg',
		],
	)


pre_mkt_content = PreMarketContent(
		target_date='July 24, 2016 12:00:01',
		target_pic='images/resources/eileen/premarket/soon.jpg',
		)


signatrue_products = [
	SignatrueProduct(
			picture='images/resources/eileen/product/1.jpg',
			title='设计师环保活页笔记本夹',
			subtitle='标志产品',
			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
			shop_link='http://notebook_shop_link',
		),
	SignatrueProduct(
			picture='images/resources/eileen/product/2.jpg',
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
		name='Eileen Sullivan',
		profile_images=profile_images,
		is_active=True,
		on_market=False,
		origin='NEW YORK',
		intro=intro,
		bio=bio,
		experience_content=experience_content,
		exclusive_content=exclusive_content,
		pre_mkt_content=pre_mkt_content,
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
		# signatrue_pics=[
		# 	'images/resources/eileen/collections/201607/signature/pics/1.jpg',
		# 	'images/resources/eileen/collections/201607/signature/pics/2.jpg',
		# ],
		# signatrue_videos=[
		# 	Video(
		# 		thumbnail='images/resources/eileen/collections/201607/signature/videos/thumbnail.png',
		# 		poster='images/resources/eileen/collections/201607/signature/videos/thumbnail.jpg',
		# 		url='images/resources/eileen/collections/201607/signature/videos/MaxMara.mp4',
		# 	)
		# ],
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
		# 	'images/resources/eileen/images/modeflip/collections/june/signature/1.jpg',
		# 	'images/resources/eileen/images/modeflip/collections/june/signature/2.jpg',
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
				pic = Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='images/resources/eileen/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='images/resources/eileen/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='images/resources/eileen/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='images/resources/eileen/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_july_2 = Garment(
				gid=2,
				cid=CID_2,
				did=DID,
				price=888,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='images/resources/eileen/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='images/resources/eileen/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='images/resources/eileen/collections/201607/garments/2/details/2.jpg'),
						]
				)



g_june_1 = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='images/resources/eileen/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='images/resources/eileen/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='images/resources/eileen/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='images/resources/eileen/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_june_2 = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/eileen/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='images/resources/eileen/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='images/resources/eileen/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='images/resources/eileen/collections/201607/garments/2/details/2.jpg'),
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