from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.models.statistics import *

local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

sc = StatisticsConfig(config_db)

dids = [1, 2, 3]
[sc.set(Statistics(did=did)) for did in dids]