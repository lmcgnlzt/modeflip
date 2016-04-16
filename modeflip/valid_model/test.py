# from pprint import pprint
import datetime

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import Designer, DesignerConfig
from modeflip.models.collection import Collection, CollectionConfig
from modeflip.models.garment import Garment, GarmentConfig



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)


dc = DesignerConfig(get_database('mf_config'))
cc = CollectionConfig(get_database('mf_config'))
gc = GarmentConfig(get_database('mf_config'))


desc1 = "Ladies handwoven rayon fully lined jacket with contrasting silk/rayon velvet notched collar and cuffs. Side seam pockets with 4-bone button closure and polyester lining. XS-XL. Made in USA"
g1 = Garment(
	gid=1,
	cid=1,
	did=1,
	price=700.00,
	description="Womans notch collar jacket, with contrast collar and cuffs",
	shop_link='https://wap.koudaitong.com/v2/showcase/goods?alias=26u1h3ut7z8xv&activity=&ps=320',
	pictures=[
		'http://modeflip.oss-cn-beijing.aliyuncs.com/EDIE%20new%20york%20images.001.jpeg',
		'http://modeflip.oss-cn-beijing.aliyuncs.com/EDIE%20new%20york%20images.002.jpeg',
		]
	)
g2 = Garment(
	gid=2,
	cid=1,
	did=1,
	price=800.00,
	description=desc1,
	shop_link='https://wap.koudaitong.com/v2/showcase/goods?alias=26u1h3ut7z8xv&activity=&ps=320',
	pictures=[
		'http://modeflip.oss-cn-beijing.aliyuncs.com/EDIE%20new%20york%20images.003.jpeg',
		'http://modeflip.oss-cn-beijing.aliyuncs.com/EDIE%20new%20york%20images.004.jpeg',
		]
	)
c1 = Collection(
	cid=1,
	did=1,
	name='2016 Spring',
	released=datetime.datetime(2016, 5, 1),
	signatrue_videos=['http://modeflip.oss-cn-beijing.aliyuncs.com/Burberry_Spring_2016.mp4'],
	signatrue_musics=['http://modeflip.oss-cn-beijing.aliyuncs.com/Fashion_Show_Music.mp3'],
	)


c2 = Collection(cid=2, did=1, name='2016 Winter', released=datetime.datetime(2016, 11, 1))


bio1 = "Sophia Tezel was born April 9, 1963 in New York City. Marc's life was completely altered following the death of his father at the age of 7. He would eventually move in with his grandmother and that made all the difference. Marc entered the Parsons School of Design and later a position at Perry Ellis. Jacobs started his own label and continued to impress the fashion world"
d1 = Designer(
		did=1,
		name='Sophia Tezel',
		origin='NEW YORK',
		is_active=True,
		icon_link="http://modeflip.oss-cn-beijing.aliyuncs.com/sophia_tezel_icon.jpg",
		bio=bio1
		)



g3 = Garment(
	gid=1,
	cid=1,
	did=2,
	price=666.00,
	description='2016 Fall Garment',
	shop_link='https://wap.koudaitong.com/v2/showcase/goods?alias=26u1h3ut7z8xv&activity=&ps=320',
	pictures=[
		'http://modeflip.oss-cn-beijing.aliyuncs.com/img1.JPG'
		]
	)

c3 = Collection(cid=1, did=2, name='2016 Fall', released=datetime.datetime(2016, 8, 15))

bio2 = "Reem Acra's designs epitomize global glamour by offering women her innate fashion sense, European style and understanding of what looks and feels beautiful. Interlaced with her sense of luxury, her regal designs are developed with a modern aesthetic. Her ready-to-wear and bridal collections evoke an ethereal quality, which appeals to a discerning clientele, including personalities, royalty and style-setting women from all over the world."
d2 = Designer(
		did=2,
		name='Reem Acra',
		origin='ITALY',
		is_active=True,
		icon_link="http://modeflip.oss-cn-beijing.aliyuncs.com/Reem_Acra_icon.jpg",
		bio=bio2)


g_list = [g1, g2, g3]
c_list = [c1, c2, c3]
d_list = [d1, d2]

[dc.set(d) for d in d_list]
[cc.set(c) for c in c_list]
[gc.set(g) for g in g_list]

print 'Done'


"""
- d1
	- c1
		- g1
		- g2
	- c2


- d2
	- c3
		- g3
"""