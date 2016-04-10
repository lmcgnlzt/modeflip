from pprint import pprint
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

d1 = Designer(did=1, name='Sophia Tezel', origin='NEW YORK', is_active=True, bio='Something about me....')
c1 = Collection(cid=1, did=1, name='2016 Spring', released=datetime.datetime(2016, 3, 1))
g1 = Garment(gid=1, cid=1, did=1, price=105.5, description='first')
g2 = Garment(gid=2, cid=1, did=1, price=22, description='second')

c2 = Collection(cid=2, did=1, name='2016 New Year', released=datetime.datetime(2016, 1, 1))
c3 = Collection(cid=3, did=1, name='2016 Fall', released=datetime.datetime(2016, 8, 15))

d1 = dc.set(d1)
c1 = cc.set(c1)
c2 = cc.set(c2)
c3 = cc.set(c3)
g1 = gc.set(g1)
g2 = gc.set(g2)

# pprint(d1.__json__())
# pprint(c1.__json__())
# pprint(c2.__json__())
# pprint(g1.__json__())
# pprint(g2.__json__())


# print dc.get_likes(1)
# print dc.get_subscribes(1)
# print dc.get_all_designers()
# print dc.do_like(1)
# print dc.do_subscribe(1)

# print cc.get(1, 1)
for c in cc.get_all_collections_by_designer(1):
	print c.released
