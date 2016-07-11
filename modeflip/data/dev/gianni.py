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
DID = 3


intro = "Gianni Guaglianone，来自意大利，Maxmara 全球设计总监，原Cerruti 1881（卓诺迪/切瑞蒂）首席设计总监，Donna Karan高级设计师。意大利Vogue的主编Carla Sozzani邀请Gianni参加在业内地位举足轻重的时尚大赛“谁是下一个罗马时尚大师”，Gianni在万众瞩目中赢得了比赛，获得MaxMara青睐，成为品牌的灵魂人物，意大利时尚界举足轻重的一位设计师。"
bio = """Gianni Guaglianone，来自意大利，Maxmara 全球设计总监。

|Gianni出生在意大利一个做时尚和生产的家庭，从小就对用图案自我表达的概念十分着迷，天赋异禀的他在享誉盛名的伦敦皇家艺术学院学习时尚设计专业，并习得了如何将才华通过现实技巧真正实现在一件服装设计作品中。

|在Gianni的毕业设计大秀上，作为评委前来的Cerruti 1881（卓诺迪/切瑞蒂）创始人尼诺切瑞蒂一眼相中Gianni并将他收入麾下，Gianni就这样加入了一个男装品牌，并成功地在任职两年内将销售提高了40%，为这个意大利经典男装品牌增添了新鲜的色彩。

|在Cerruti在米兰的的一场大秀中，来自纽约的著名时装设计师Donna Karan在第一排看秀，并被Gianni为品牌带来的改变而惊喜万分，在秀结束时便邀请Gianni加入她的设计团队，当时Donna Karan刚刚被Louis Vuitton集团收购正在准备重磅推出全新的男装系列，而Gianni的加入让新系列如虎添翼。

|2006年，出于一直以来对女装设计的热爱，Gianni开始构思自己的女装品牌，当时意大利Vogue的主编Carla Sozzani邀请Gianni参加在业内地位举足轻重的时尚大赛“谁是下一个罗马时尚大师”，Gianni在万众瞩目中赢得了比赛，并在赛后拿到了MaxMara投来的橄榄枝，正式加入MaxMara担任全球首席设计总监，开始谱写至今长达九年的传奇篇章，在第一年便将销量提升32%，同时将品牌带到了亚洲市场。
"""

profile_images = ProfileImages(
		icon_url='images/resources/gianni/icon/icon.jpg',
		image_url='images/resources/gianni/icon/image.jpg',
		background_url='images/resources/gianni/icon/background.jpg',
	)

pics = [Picture(thumbnail='images/resources/gianni/experience/pics/{}s.jpg'.format(i), image='images/resources/gianni/experience/pics/{}.jpg'.format(i)) for i in range(0, 74) if os.path.isfile('/Users/mli/modeapp/modeapp/static/images/resources/gianni/experience/pics/{}s.jpg'.format(i))]
sig_pics = random.sample(pics, 24)

experience_content = ExperienceContent(
	brands=[
		'images/resources/gianni/experience/brand/cerruti.jpg',
		'images/resources/gianni/experience/brand/dkny.jpg',
		'images/resources/gianni/experience/brand/maxmara.jpg',
		'images/resources/gianni/experience/brand/gianni.jpg',
		],
	sig_pics = sig_pics,
	pics = pics,
	videos=[
		Video(
				thumbnail='images/resources/gianni/experience/videos/thumbnail.png',
				poster='images/resources/gianni/experience/videos/thumbnail.jpg',
				url='images/resources/gianni/experience/videos/MaxMara.mp4',
			)
		]
	)


exclusive_content = ExclusiveContent(
	title='独家签约 -- Exclusive Collections',
	pics=[
		'images/resources/gianni/exclusive/pics/1.jpg',
		],
	)


pre_mkt_content = PreMarketContent(
		target_date='July 20, 2016 12:00:00',
		target_pic='images/resources/gianni/premarket/soon.jpg',
		)


signatrue_products = [
	SignatrueProduct(
			picture='images/resources/gianni/product/1.jpg',
			title='设计师环保活页笔记本夹',
			subtitle='标志产品',
			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
			shop_link='http://notebook_shop_link',
		),
	SignatrueProduct(
			picture='images/resources/gianni/product/2.jpg',
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
		name='Gianni Guaglianone',
		profile_images=profile_images,
		is_active=True,
		on_market=False,
		origin='意大利',
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
		# 	'images/resources/gianni/collections/201607/signature/pics/1.jpg',
		# 	'images/resources/gianni/collections/201607/signature/pics/2.jpg',
		# ],
		# signatrue_videos=[
		# 	Video(
		# 		thumbnail='images/resources/gianni/collections/201607/signature/videos/thumbnail.png',
		# 		poster='images/resources/gianni/collections/201607/signature/videos/thumbnail.jpg',
		# 		url='images/resources/gianni/collections/201607/signature/videos/MaxMara.mp4',
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
		# 	'images/resources/gianni/images/modeflip/collections/june/signature/1.jpg',
		# 	'images/resources/gianni/images/modeflip/collections/june/signature/2.jpg',
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
				pic = Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='images/resources/gianni/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='images/resources/gianni/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='images/resources/gianni/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='images/resources/gianni/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_july_2 = Garment(
				gid=2,
				cid=CID_2,
				did=DID,
				price=888,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='images/resources/gianni/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='images/resources/gianni/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='images/resources/gianni/collections/201607/garments/2/details/2.jpg'),
						]
				)



g_june_1 = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
					Picture(title="细节1", image='images/resources/gianni/collections/201607/garments/1/details/1.jpg'),
					Picture(title="细节2", image='images/resources/gianni/collections/201607/garments/1/details/2.jpg'),
					Picture(title="细节3", image='images/resources/gianni/collections/201607/garments/1/details/3.jpg'),
					Picture(title="细节4", image='images/resources/gianni/collections/201607/garments/1/details/4.jpg'),
						]
				)


g_june_2 = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=777,
				shop_link='http://shop_link',
				pic = Picture(title="蕾丝花边裙", image='images/resources/gianni/collections/201607/garments/1/pre1.jpg'),
				details=[
					Picture(title="无袖开衩长裙", image='images/resources/gianni/collections/201607/garments/2/1s.jpg'),
					Picture(title="细节1", image='images/resources/gianni/collections/201607/garments/2/details/1.jpg'),
					Picture(title="细节2", image='images/resources/gianni/collections/201607/garments/2/details/2.jpg'),
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