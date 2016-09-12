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

thumbnails_ids = [24, 45, 6, 44, 14, 46, 49, 38]
thumbnails = ['http://assets.modeflip.com/sophia/experience/thumbnails/{}s.jpg'.format(i) for i in thumbnails_ids]

ids = ['0', '1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '18', '19', '20', '21', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '40', '41', '42', '43', '44', '45', '46']
pics = [Picture(thumbnail='http://assets.modeflip.com/sophia/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/sophia/experience/pics/{}.jpg'.format(i)) for i in thumbnails_ids ]
[pics.append(Picture(thumbnail='http://assets.modeflip.com/sophia/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/sophia/experience/pics/{}.jpg'.format(i))) for i in ids if i not in thumbnails_ids]

experience_content = ExperienceContent(
	brands=[
		'http://assets.modeflip.com/sophia/experience/brand/burberry.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/juicy.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/r_minkoff.jpg',
		'http://assets.modeflip.com/sophia/experience/brand/sophia.jpg',
		],
	thumbnails=thumbnails,
	pics=pics,
	# videos=[
	# 	Video(
	# 			thumbnail='http://assets.modeflip.com/sophia/experience/videos/thumbnail.png',
	# 			poster='http://assets.modeflip.com/sophia/experience/videos/thumbnail.jpg',
	# 			url='http://assets.modeflip.com/sophia/experience/videos/MaxMara.mp4',
	# 		)
	# 	]
	)


exclusive_content = ExclusiveContent(
	pics=[
		'http://assets.modeflip.com/sophia/exclusive/pics/1.jpg',
		],
	)


# pre_mkt_content = PreMarketContent(
# 		target_date='July 25, 2016 10:00:01',
# 		target_pic='http://assets.modeflip.com/sophia/premarket/soon.jpg',
# 		)


# signatrue_products = [
# 	SignatrueProduct(
# 			picture='http://assets.modeflip.com/sophia/product/1.jpg',
# 			title='设计师环保活页笔记本夹',
# 			subtitle='标志产品',
# 			desc='这是一段关于活页笔记本夹的简要介绍，字体可以调整',
# 			shop_link='http://notebook_shop_link',
# 		),
# 	SignatrueProduct(
# 			picture='http://assets.modeflip.com/sophia/product/2.jpg',
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
		name='Sophia Tezel',
		profile_images=profile_images,
		is_active=True,
		on_market=True,
		origin='NEW YORK',
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


sophia_collections = Collection(
		cid=CID_1,
		did=DID,
		title='SOPHIA TEZEL',
		desc='作为好莱坞女星最爱的设计师之一，Sophia的设计总是受到好莱坞明星和歌手的青睐，包括Taylor Swift,暮光之城女主角Christine Stewart、纽约第一社交名媛Olivia Palermo（gossip girl现实版）、Sex and the City女主角Sarah Jessica Parker、维密天使Miranda Kerr等等。',
		released=datetime(2016, 7, 25),
		signatrue_pics=[
			'http://assets.modeflip.com/sophia/collections/sophiacollections/signature/pics/1.jpg',
			'http://assets.modeflip.com/sophia/collections/sophiacollections/signature/pics/2.jpg',
		],
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
	sophia_collections,
]

[cc.set(c) for c in collections]
print 'collection info saved'




############################################################################################################


fiona_pants = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=735,
				shop_link='https://wap.koudaitong.com/v2/goods/277ly787ymf1v',
				pic = Picture(title="Fiona Pants - 阔腿裤", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/7.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/8.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/9.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants/details/10.jpg'),
						]
				)


diana_top = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=813,
				shop_link='https://wap.koudaitong.com/v2/goods/3f0arh7vkfqeb',
				pic = Picture(title="Diana Top - 蕾丝上衣", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/7.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/8.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top/details/9.jpg'),
						]
				)


anne_skirt = Garment(
				gid=3,
				cid=CID_1,
				did=DID,
				price=780,
				shop_link='https://wap.koudaitong.com/v2/goods/3enymaetx4k4j',
				pic = Picture(title="Anne Skirt - 百褶裙", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/anne_skirt/details/5.jpg'),
						]
				)


corrine_shirt_black = Garment(
				gid=4,
				cid=CID_1,
				did=DID,
				price=682,
				shop_link='https://wap.koudaitong.com/v2/goods/2frleanqm1fpf',
				pic = Picture(title="Corrine Shirt - 衬衫(黑色)", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_black/details/6.jpg'),
						]
				)


corrine_shirt_white = Garment(
				gid=5,
				cid=CID_1,
				did=DID,
				price=682,
				shop_link='https://wap.koudaitong.com/v2/goods/2xbg9oeh5ieoj',
				pic = Picture(title="Corrine Shirt - 衬衫(白色)", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/corrine_shirt_white/details/6.jpg'),
						]
				)


diana_top_blue = Garment(
				gid=6,
				cid=CID_1,
				did=DID,
				price=813,
				shop_link='https://wap.koudaitong.com/v2/goods/1y2r95tvpc0o3',
				pic = Picture(title="Diana Top - 蕾丝上衣(蓝色)", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/diana_top_blue/details/6.jpg'),
						]
				)


fiona_dress = Garment(
				gid=7,
				cid=CID_1,
				did=DID,
				price=910,
				shop_link='https://wap.koudaitong.com/v2/goods/364245n7v25lv',
				pic = Picture(title="Fiona Dress - 连衣裙", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_dress/details/7.jpg'),
						]
				)


kelly_dress = Garment(
				gid=8,
				cid=CID_1,
				did=DID,
				price=850,
				shop_link='https://wap.koudaitong.com/v2/goods/2frkcz73cc6f7',
				pic = Picture(title="Kelly Dress - 连衣裙", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/kelly_dress/details/6.jpg'),
						]
				)


cappa_black = Garment(
				gid=9,
				cid=CID_1,
				did=DID,
				price=680,
				shop_link='https://wap.koudaitong.com/v2/goods/3f0bz097p3uqr',
				pic = Picture(title="Cappa Black - 披肩", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_black/details/6.jpg'),
						]
				)


cappa_blue = Garment(
				gid=10,
				cid=CID_1,
				did=DID,
				price=680,
				shop_link='https://wap.koudaitong.com/v2/goods/361l9h4hu41pv',
				pic = Picture(title="Cappa Blue - 披肩", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/cappa_blue/details/6.jpg'),
						]
				)


fiona_pants_blue = Garment(
				gid=11,
				cid=CID_1,
				did=DID,
				price=735,
				shop_link='https://wap.koudaitong.com/v2/goods/1y7ogg4xp6mcz',
				pic = Picture(title="Fiona Pants Blue - 阔腿裤", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/fiona_pants_blue/details/4.jpg'),
						]
				)


hellen_dress = Garment(
				gid=12,
				cid=CID_1,
				did=DID,
				price=990,
				shop_link='https://wap.koudaitong.com/v2/goods/3ewlwiecsmotv',
				pic = Picture(title="Hellen Dress - 连衣裙", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_dress/details/4.jpg'),
						]
				)


hellen_sundress = Garment(
				gid=13,
				cid=CID_1,
				did=DID,
				price=860,
				shop_link='https://wap.koudaitong.com/v2/goods/3f1ikzrec8rz7',
				pic = Picture(title="Hellen Sundress - 太阳裙", image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/details/0.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/sophia/collections/sophiacollections/garments/hellen_sundress/details/4.jpg'),
						]
				)


garments = [
	fiona_pants,
	diana_top,
	anne_skirt,
	corrine_shirt_black,
	corrine_shirt_white,
	diana_top_blue,
	fiona_dress,
	kelly_dress,
	cappa_black,
	cappa_blue,
	fiona_pants_blue,
	hellen_dress,
	hellen_sundress,
]

[gc.set(g) for g in garments]
print 'garments info saved'