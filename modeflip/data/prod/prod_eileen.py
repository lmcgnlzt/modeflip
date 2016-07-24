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
DID = 1


intro = "来自纽约，Ralph Lauren全球设计副总裁22年，和Ralph先生一起建立起Ralph Lauren时尚帝国，同时被大名鼎鼎的唐纳川普（Donald John Trump）的女儿伊万卡川普 (Ivanka Trump)钦点，为其同名时尚品牌伊凡卡川普担任创意总监。目前担任着FIT时尚设计学院的客座讲师，是美国具有重要地位的设计师。"
bio = """Eileen Sullivan，来自纽约，任Ralph Lauren全球设计副总裁22年，与Ralph先生一起建立起Ralph Lauren时尚帝国。

|Eileen在巴黎和伦敦长大，从时尚设计专业毕业后，便被美国最经典奢侈品Ralph Lauren钦点，随后作为Ralph先生的左膀右臂任命全球设计副总裁。

|在22年中，Eileen重新定义了RL品牌的美国休闲服装风格，在她的设计管理下，Ralph Lauren在全球范围内开创了Polo Ralph Lauren的顶级经典的系列，包括RL蓝标、童装、运动、内衣、泳装、高尔夫等等。

|Eileen同时被大名鼎鼎的唐纳川普(Donald Trump) 的女儿伊凡卡川普 (Ivanka Trump) 钦点，为其同名时尚品牌伊凡卡川普担任创意总监。

|Eileen现在住在美国东岸的玛莎葡萄园岛，带来她自有品牌，Love for Edie及SquibeeS，同时担任着FIT时尚设计学院的客座讲师，是美国具有重要地位的设计师。
"""

profile_images = ProfileImages(
		icon_url='http://assets.modeflip.com/eileen/icon/icon.jpg',
		image_url='http://assets.modeflip.com/eileen/icon/image.jpg',
		background_url='http://assets.modeflip.com/eileen/icon/background.jpg',
	)

ids = ['0', '1', '3', '4', '5', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '50', '51', '52']
pics = [Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/eileen/experience/pics/{}.jpg'.format(i)) for i in ids]

sig_pics_ids = [1, 14, 3, 13, 5, 4, 15, 16, 17, 18, 19, 20, 21, 22, 23, 52]
sig_pics = [Picture(thumbnail='http://assets.modeflip.com/eileen/experience/pics/{}s.jpg'.format(i), image='http://assets.modeflip.com/eileen/experience/pics/{}.jpg'.format(i)) for i in sig_pics_ids]


experience_content = ExperienceContent(
	brands=[
		'http://assets.modeflip.com/eileen/experience/brand/rl.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/eide.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/squibees.jpg',
		'http://assets.modeflip.com/eileen/experience/brand/trump.jpg',
		],
	sig_pics = sig_pics,
	pics = pics,
	videos=[
		Video(
				thumbnail='http://assets.modeflip.com/eileen/experience/videos/thumbnail.png',
				poster='http://assets.modeflip.com/eileen/experience/videos/thumbnail.jpg',
				url='http://assets.modeflip.com/eileen/experience/videos/MaxMara.mp4',
			)
		]
	)


exclusive_content = ExclusiveContent(
	title='独家签约 -- Exclusive Collections',
	pics=[
		'http://assets.modeflip.com/eileen/exclusive/pics/1.jpg',
		],
	)


pre_mkt_content = PreMarketContent(
		target_date='July 24, 2016 12:00:01',
		target_pic='http://assets.modeflip.com/eileen/premarket/soon.jpg',
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
		name='Eileen Sullivan',
		profile_images=profile_images,
		is_active=True,
		on_market=True,
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

edie_collections = Collection(
		cid=CID_1,
		did=DID,
		title='Love for Edie 系列',
		desc='Eileen为MODE FLIP独家推出的"Love for Edie"品牌限量系列，重塑美国60年代当红影星Edie Sedgwick迷人的复古气质，时髦性感又点天真',
		released=datetime(2016, 7, 24),
		signatrue_pics=[
			'http://assets.modeflip.com/eileen/collections/edie/signature/pics/edie1.jpg',
			'http://assets.modeflip.com/eileen/collections/edie/signature/pics/edie2.jpg',
			'http://assets.modeflip.com/eileen/collections/edie/signature/pics/edie3.jpg',
			'http://assets.modeflip.com/eileen/collections/edie/signature/pics/edie4.jpg',
		],
		signatrue_videos=[
			Video(
				thumbnail='http://assets.modeflip.com/eileen/collections/edie/signature/videos/edie_1.jpg',
				poster='http://assets.modeflip.com/eileen/collections/edie/signature/videos/edie_1.jpg',
				url='http://assets.modeflip.com/eileen/collections/edie/signature/videos/edie_1.mp4',
			)
		],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=True,
		)


CID_2 = 2
squibees_collections = Collection(
		cid=CID_2,
		did=DID,
		title='SquibeeS 系列',
		desc='Elieen带来了来自Martha`s Vineyard(美国玛莎葡萄园岛）独特风情的SquibeeS品牌系列。在lambert Cove沙滩，享受全年充足的日照，白天帆船，冲浪；日落夜出，跟随街上的盛大的彩灯及欢乐的游行活动，躺在沙滩上看天空中燃放的烟花。SquibeeS，365天都是夏季一般阳光爽朗的好心情，顺便悄悄告诉你，好莱坞明星，艺术家，音乐家，政治家居住于此！',
		released=datetime(2016, 7, 24),
		signatrue_pics=[
			'http://assets.modeflip.com/eileen/collections/squibees/signature/pics/1.jpg',
			'http://assets.modeflip.com/eileen/collections/squibees/signature/pics/2.jpg',
			'http://assets.modeflip.com/eileen/collections/squibees/signature/pics/3.jpg',
			'http://assets.modeflip.com/eileen/collections/squibees/signature/pics/4.jpg',
			'http://assets.modeflip.com/eileen/collections/squibees/signature/pics/5.jpg',
		],
		# signatrue_videos=[
		# 	Video(
		# 		thumbnail='http://assets.modeflip.com/eileen/collections/201607/signature/videos/thumbnail.png',
		# 		poster='http://assets.modeflip.com/eileen/collections/201607/signature/videos/thumbnail.jpg',
		# 		url='http://assets.modeflip.com/eileen/collections/201607/signature/videos/MaxMara.mp4',
		# 	)
		# ],
		# signatrue_musics=[
		# 	'http://sig_music_1.com',
		# 	'http://sig_music_2.com',
		# ],
		new_arrival=True,
		)





collections = [
	edie_collections,
	squibees_collections,
]

[cc.set(c) for c in collections]
print 'collection info saved'




############################################################################################################


bella_dress = Garment(
				gid=1,
				cid=CID_1,
				did=DID,
				price=799,
				shop_link='https://wap.koudaitong.com/v2/goods/2fyy90xwhees3',
				pic = Picture(title="Bella Dress - 小黑裙", image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/bella_dress/details/6.jpg'),
						]
				)


sophia_dress = Garment(
				gid=2,
				cid=CID_1,
				did=DID,
				price=978,
				shop_link='https://wap.koudaitong.com/v2/goods/27cimy90r96er',
				pic = Picture(title="Sophia Dress - 连衣裙", image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/edie/garments/sophia_dress/details/6.jpg'),
						]
				)


anna_dress = Garment(
				gid=3,
				cid=CID_2,
				did=DID,
				price=860,
				shop_link='https://wap.koudaitong.com/v2/goods/2fnvbq4tfd99f',
				pic = Picture(title="Anna Dress - 连衣裙", image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/anna_dress/details/7.jpg'),
						]
				)

pippa_skirt = Garment(
				gid=4,
				cid=CID_2,
				did=DID,
				price=738,
				shop_link='https://wap.koudaitong.com/v2/goods/3np6vyfkgazpf',
				pic = Picture(title="Pippa Skirt - 百褶裙", image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/cover.jpg'),
				details=[
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/1.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/2.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/3.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/4.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/5.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/6.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/7.jpg'),
					Picture(image='http://assets.modeflip.com/eileen/collections/squibees/garments/pippa_skirt/details/8.jpg'),
						]
				)




garments = [
	bella_dress,
	sophia_dress,
	anna_dress,
	pippa_skirt,
]

[gc.set(g) for g in garments]
print 'garments info saved'