#coding=utf-8

import os.path
import random

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


intro = "来自意大利，Maxmara 全球设计总监，原Cerruti 1881（卓诺迪/切瑞蒂）首席设计总监，Donna Karan高级设计师。意大利Vogue的主编Carla Sozzani邀请Gianni参加在业内地位举足轻重的时尚大赛“谁是下一个罗马时尚大师”，Gianni在万众瞩目中赢得了比赛，获得MaxMara青睐，成为品牌的灵魂人物，意大利时尚界举足轻重的一位设计师。"
bio = """Gianni Guaglianone，来自意大利，Maxmara 全球设计总监。

|Gianni出生在意大利一个做时尚和生产的家庭，从小就对用图案自我表达的概念十分着迷，天赋异禀的他在享誉盛名的伦敦皇家艺术学院学习时尚设计专业，并习得了如何将才华通过现实技巧真正实现在一件服装设计作品中。

|在Gianni的毕业设计大秀上，作为评委前来的Cerruti 1881（卓诺迪/切瑞蒂）创始人尼诺切瑞蒂一眼相中Gianni并将他收入麾下，Gianni就这样加入了一个男装品牌，并成功地在任职两年内将销售提高了40%，为这个意大利经典男装品牌增添了新鲜的色彩。

|在Cerruti在米兰的的一场大秀中，来自纽约的著名时装设计师Donna Karan在第一排看秀，并被Gianni为品牌带来的改变而惊喜万分，在秀结束时便邀请Gianni加入她的设计团队，当时Donna Karan刚刚被Louis Vuitton集团收购正在准备重磅推出全新的男装系列，而Gianni的加入让新系列如虎添翼。

|2006年，出于一直以来对女装设计的热爱，Gianni开始构思自己的女装品牌，当时意大利Vogue的主编Carla Sozzani邀请Gianni参加在业内地位举足轻重的时尚大赛“谁是下一个罗马时尚大师”，Gianni在万众瞩目中赢得了比赛，并在赛后拿到了MaxMara投来的橄榄枝，正式加入MaxMara担任全球首席设计总监，开始谱写至今长达九年的传奇篇章，在第一年便将销量提升32%，同时将品牌带到了亚洲市场。
"""

profile_images = ProfileImages(
		icon_url='http://assets.modeflip.com/gianni/icon/icon.jpg',
		image_url='http://assets.modeflip.com/gianni/icon/image.jpg',
		background_url='http://assets.modeflip.com/gianni/icon/background.jpg',
	)

thumbnails_ids = [4, 49, 5, 3, 2, 11, 54, 8]
thumbnails = ['http://assets.modeflip.com/gianni/experience/thumbnails/{}s.jpg'.format(i) for i in thumbnails_ids]

ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '25', '26', '27', '28', '29', '30', '31', '32', '33', '35', '36', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '63', '64', '65', '66', '68', '70', '71', '72', '73']
pics = [Picture(thumbnail='http://assets.modeflip.com/gianni/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/gianni/experience/pics/{}.jpg'.format(i)) for i in thumbnails_ids ]
[pics.append(Picture(thumbnail='http://assets.modeflip.com/gianni/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/gianni/experience/pics/{}.jpg'.format(i))) for i in ids if i not in thumbnails_ids]


experience_content = ExperienceContent(
	brands=[
		'http://assets.modeflip.com/gianni/experience/brand/maxmara.jpg',
		'http://assets.modeflip.com/gianni/experience/brand/cerruti.jpg',
		'http://assets.modeflip.com/gianni/experience/brand/dkny.jpg',
		'http://assets.modeflip.com/gianni/experience/brand/gianni.jpg',
		],
	thumbnails=thumbnails,
	pics=pics,
	# videos=[
	# 	Video(
	# 			thumbnail='http://assets.modeflip.com/gianni/experience/videos/thumbnail.png',
	# 			poster='http://assets.modeflip.com/gianni/experience/videos/thumbnail.jpg',
	# 			url='http://assets.modeflip.com/gianni/experience/videos/MaxMara.mp4',
	# 		)
	# 	]
	)


exclusive_content = ExclusiveContent(
	pics=[
		'http://assets.modeflip.com/gianni/exclusive/pics/1.jpg',
		],
	)


# pre_mkt_content = PreMarketContent(
# 		target_date='July 30, 2016 12:00:01',
# 		target_pic='http://assets.modeflip.com/gianni/premarket/soon.jpg',
# 		)


# signatrue_products = [
# 	SignatrueProduct(
# 			picture='http://assets.modeflip.com/gianni/product/1.jpg',
# 			title='设计师环保活页笔记本夹',
# 			subtitle='标志产品',
# 			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
# 			shop_link='http://notebook_shop_link',
# 		),
# 	SignatrueProduct(
# 			picture='http://assets.modeflip.com/gianni/product/2.jpg',
# 			title='A5 设计师独家设计卡',
# 			# subtitle='Signature Product',
# 			# desc='This is an awesome notebook, you will love it',
# 			shop_link='http://notebook_shop_link',
# 		),
# 	]

# private_musics = [
# 	PrivateMusic(
# 		music_icon='http://music_icon_1.com',
# 		title='Ugly Is Beautiful',
# 		author='David Usher',
# 		link='http://private_music_1.com'
# 		),
# 	PrivateMusic(
# 		music_icon='http://music_icon_2.com',
# 		title='Beautiful Is Ugly',
# 		author='Usher David',
# 		link='http://private_music_2.com'
# 		),
# 	]


d = Designer(
		did=DID,
		name='Gianni Guaglianone',
		profile_images=profile_images,
		is_active=True,
		on_market=True,
		origin='ITALY',
		intro=intro,
		bio=bio,
		experience_content=experience_content,
		exclusive_content=exclusive_content,
		# pre_mkt_content=pre_mkt_content,
		# signatrue_products=signatrue_products,
		# private_musics=private_musics,
		)


dc.set(d)

print 'designer info saved'



############################################################################################################
CID_1 = 1


littleblackdress_colltion = Collection(
		cid=CID_1,
		did=DID,
		title='Little Black Dress',
		desc='“Every woman should own a simple elegant black dress”。Gianni独家设计命名的优雅小黑裙仅在MODE FLIP平价发售，再现Maxmara经典小黑裙',
		released=datetime(2016, 7, 24),
		signatrue_pics=[
			'http://assets.modeflip.com/gianni/collections/littleblackdress/signature/pics/1.jpg',
			'http://assets.modeflip.com/gianni/collections/littleblackdress/signature/pics/2.jpg',
		],
		# signatrue_videos=[
		# 	Video(
		# 		thumbnail='http://assets.modeflip.com/gianni/collections/201607/signature/videos/thumbnail.png',
		# 		poster='http://assets.modeflip.com/gianni/collections/201607/signature/videos/thumbnail.jpg',
		# 		url='http://assets.modeflip.com/gianni/collections/201607/signature/videos/MaxMara.mp4',
		# 	)
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=True,
		)




collections = [
	littleblackdress_colltion,
]

[cc.set(c) for c in collections]
print 'collection info saved'




############################################################################################################


aglaya_dress = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=870,
				shop_link='https://wap.koudaitong.com/v2/goods/362t31f5jo1ab',
				pic = Picture(title="Aglaya Dress - 小黑裙", image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/7.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/aglaya_dress/details/8.jpg'),
						]
				)


albina_dress = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=960,
				shop_link='https://wap.koudaitong.com/v2/goods/3erpdz1g2szc3',
				pic = Picture(title="Albina Dress - 小黑裙", image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/albina_dress/details/6.jpg'),
						]
				)


antonina_dress = Garment(
				gid=3,
				cid=CID_1,
				did=DID,
				price=980,
				shop_link='https://wap.koudaitong.com/v2/goods/1yhhtnkv6fjpf',
				pic = Picture(title="Antonina Dress - 小黑裙", image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/antonina_dress/details/7.jpg'),
						]
				)


anastasia_dress = Garment(
				gid=4,
				cid=CID_1,
				did=DID,
				price=950,
				shop_link='https://wap.koudaitong.com/v2/goods/2fxp7jjk9nes3',
				pic = Picture(title="Anastasia Dress - 小黑裙", image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/cover.jpg'),
				details=[
					# Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/7.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/8.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/9.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/10.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/11.jpg'),
					Picture(image='http://assets.modeflip.com/gianni/collections/littleblackdress/garments/anastasia_dress/details/12.jpg'),
						]
				)



garments = [
	aglaya_dress,
	albina_dress,
	antonina_dress,
]

[gc.set(g) for g in garments]
print 'garments info saved'