from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.models.designer import Designer, DesignerConfig
from modeflip.models.collection import Collection, CollectionConfig
from modeflip.models.garment import Garment, GarmentConfig
from modeflip.models.statistics import Statistics, StatisticsConfig


local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')


dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)


meta = []

dids = dc.get_all_ids()
for did in dids:
	meta.append('did')
	meta.append(did)
	cids = cc.get_all_ids(did)
	for cid in cids:
		meta.append('cid')
		meta.append(cid)

		gids = gc.get_all_ids(did, cid)
		meta.append('gid')
		for gid in gids:
			meta.append(gid)

print meta




# [(1), (1, 1), (1, 1, 1), (1, 1, 2)]

# ['d', 1, 'c', 1, 'g', 1, 2, 3]
# [1, 2, ]




# d1, c1, g1, g2, g3, g4, g5, c2, g1, g2,

# d1, c1, g1, g2, g3, c2, g1, g2, d2, c1,

# d1, (d1, c1), (d1, c1, g1), (d1, c1, g2), (d1, c2, g3), (d1, c2), (d1, c2, g1), (d1, c2, g2), d2, (d2, c1), (d2, c1, g1)