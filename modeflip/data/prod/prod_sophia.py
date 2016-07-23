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
DID = 3


intro = "来自纽约，Burberry全球时尚顾问，Juicy Couture，Rebecca Minkoff全球设计总监，好莱坞女星及歌手最爱的设计师之一，包括Taylor Swift,暮光之城女主角Christine Stewart、纽约第一社交名媛Olivia Palermo（gossip girl现实版）、Sex and the City女主角Sarah Jessica Parker、维密天使Miranda Kerr等。"
bio = """Sophia Tezel，来自纽约，Burberry全球时尚顾问，Juicy Couture，Rebecca Minkoff全球设计总监。

|Sophia Tezel从小在爸妈的服装工厂长大，耳濡目染下拥有了对时尚敏锐的嗅觉，和对工艺精巧的把握，并将这些渗透她的每一件设计作品之中。她认为时尚应该是美与实穿的结合，是有着让人惊艳的细节而让人总想再多看一眼。

|Sophia的身影总是出现在时尚的一线前沿，为包括Rebecca Minkoff、Nicole Miller、Juicy Couture等纽约年轻人钟爱的品牌担任设计总监，将她极高标准的国际品牌设计惊艳为品牌注入新鲜血液带来全新活力。为了达到美与实穿的完美结合，她总是倾注其才华与多年在设计开发生产的经验。她的身边永远有面料、纸板、无数的细节包围，而时至今日的她依然会为色彩、质感、工艺—所有组成一件完美服装的元素而激动和澎湃，对她而言，一件服装的诞生是一个有魔力的美好的过程。

|Sophia，在二十几岁时曾在悉尼创建自己的品牌，后来带着一颗要在世界时尚的中心大展拳脚的野心来到了美国纽约。她自己的品牌IS获得了无数的赞美和掌声，当时销往美国顶级奢侈品百货商场包括Barneys、Bergdorf Goodman、Saks等等。年轻的她很早便登上各大时尚杂志，包括Vogue、Elle、WWWD等。

|Sophia的设计总是受到好莱坞明星和歌手的青睐，包括Taylor Swift,暮光之城女主角Christine Stewart、纽约第一社交名媛Olivia Palermo（gossip girl现实版）、Sex and the City女主角Sarah Jessica Parker、维密天使Miranda Kerr等等。

|如今Sophia想用她对牛仔的热爱为时尚圈带来一个全新的牛仔品牌，并与2016年在纽约华丽亮相。"""

profile_images = ProfileImages(
		icon_url='http://assets.modeflip.com/sophia/icon/icon.jpg',
		image_url='http://assets.modeflip.com/sophia/icon/image.jpg',
		background_url='http://assets.modeflip.com/sophia/icon/background.jpg',
	)

ids = ['0', '1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '18', '19', '20', '21', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '40', '41', '42', '43', '44', '45', '46']
pics = [Picture(thumbnail='http://assets.modeflip.com/sophia/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/sophia/experience/pics/{}.jpg'.format(i)) for i in ids]

sig_pics_ids = [24, 45, 6, 44, 14, 46, 49, 38, 32, 21, 33, 34, 23, 42, 5, 20]
sig_pics = [Picture(thumbnail='http://assets.modeflip.com/sophia/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/sophia/experience/pics/{}.jpg'.format(i)) for i in sig_pics_ids]


experience_content = ExperienceContent(
	brands=[
		'http://assets.modeflip.com/sophia/experience/brand/burberry.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/juicy.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/r_minkoff.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/sophia.jpg',
		],
	sig_pics = sig_pics,
	pics = pics,
	videos=[
		Video(
				thumbnail='http://assets.modeflip.com/sophia/experience/videos/thumbnail.png',
				poster='http://assets.modeflip.com/sophia/experience/videos/thumbnail.jpg',
				url='http://assets.modeflip.com/sophia/experience/videos/MaxMara.mp4',
			)
		]
	)


exclusive_content = ExclusiveContent(
	title='独家签约 -- Exclusive Collections',
	pics=[
		'http://assets.modeflip.com/sophia/exclusive/pics/1.jpg',
		],
	)


pre_mkt_content = PreMarketContent(
		target_date='July 24, 2016 12:00:01',
		target_pic='http://assets.modeflip.com/sophia/premarket/soon.jpg',
		)


signatrue_products = [
	SignatrueProduct(
			picture='http://assets.modeflip.com/sophia/product/1.jpg',
			title='设计师环保活页笔记本夹',
			subtitle='标志产品',
			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
			shop_link='http://notebook_shop_link',
		),
	SignatrueProduct(
			picture='http://assets.modeflip.com/sophia/product/2.jpg',
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
		name='Sophia Tezel',
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
CID_1 = 1


c_aug = Collection(
		cid=CID_1,
		did=DID,
		title='八月限量主题春夏系列',
		released=datetime(2016, 7, 24),
		# signatrue_pics=[
		# 	'http://assets.modeflip.com/sophia/collections/201607/signature/pics/1.jpg',
		# 	'http://assets.modeflip.com/sophia/collections/201607/signature/pics/2.jpg',
		# ],
		# signatrue_videos=[
		# 	Video(
		# 		thumbnail='http://assets.modeflip.com/sophia/collections/201607/signature/videos/thumbnail.png',
		# 		poster='http://assets.modeflip.com/sophia/collections/201607/signature/videos/thumbnail.jpg',
		# 		url='http://assets.modeflip.com/sophia/collections/201607/signature/videos/MaxMara.mp4',
		# 	)
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=True,
		)


collections = [
	c_aug,
]

[cc.set(c) for c in collections]
print 'collection info saved'




############################################################################################################


g_aug_1 = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=888,
				shop_link='https://wap.koudaitong.com/v2/goods/2fnvbq4tfd99f',
				pic = Picture(title="白色黑色蕾丝衬衫", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/cover.jpg'),
				details=[
					Picture(title="整体正面效果", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/4.jpg'),
					Picture(title="细节1", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/5.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/6.jpg'),
					Picture(title="细节3", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/7.jpg'),
					Picture(title="细节4", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/8.jpg'),
					Picture(title="细节4", image='http://assets.modeflip.com/sophia/collections/201608/garments/1/details/9.jpg'),
						]
				)


g_aug_2 = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=888,
				shop_link='https://wap.koudaitong.com/v2/goods/3np6vyfkgazpf',
				pic = Picture(title="黑色蕾丝衬衫", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/cover.jpg'),
				details=[
					Picture(title="细节1", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/details/2.jpg'),
					Picture(title="细节2", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/details/3.jpg'),
					Picture(title="细节3", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/details/4.jpg'),
					Picture(title="细节4", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/details/5.jpg'),
					Picture(title="细节5", image='http://assets.modeflip.com/sophia/collections/201608/garments/2/details/6.jpg'),
						]
				)



garments = [
	g_aug_1,
	g_aug_2,
]

[gc.set(g) for g in garments]
print 'garments info saved'