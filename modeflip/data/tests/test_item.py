from datetime import datetime, timedelta

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *
from modeflip.models.transaction import *
from modeflip.models.merchant import *
from modeflip.models.item import *
from pprint import pprint


local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)
tc = TransactionConfig(config_db)
mc = MerchantConfig(config_db)
ic = ItemConfig(config_db)


for i in range(10):
	item = Item(
			tag='17BHC20100%s'%i,
			price=813+i,
			did=1,
			cid=1,
		)

	ic.set(item)

print ic.get_all_tags()