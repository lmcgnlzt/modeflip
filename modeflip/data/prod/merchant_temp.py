from datetime import datetime, timedelta

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *
from modeflip.models.transaction import *
from modeflip.models.merchant import *
from pprint import pprint


local_config = get_configuration('production')
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)
tc = TransactionConfig(config_db)
mc = MerchantConfig(config_db)


m = Merchant(
		user_name='temp',
		wechat_id='ZapDude',
		address='The Cloud',
		phone='00000000000'
	)


mc.set(m)

mm = mc.get_by_user_name('temp')
mm.set_password('666666')
mc.set(mm)

pprint(mm.__json__())

print mm.check_salted_password('666666')

print mc.get_by_password('temp', '666666')