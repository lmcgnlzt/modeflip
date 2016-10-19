from datetime import datetime, timedelta

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.utils.redisdb import RedisManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *
from modeflip.models.transaction import *
from modeflip.models.merchant import *
from pprint import pprint


local_config = get_configuration()
get_cache = RedisManager(local_config, force_load=True)
cache = get_cache('mf_cache')
print cache

print cache.keys()

ACCESS_TOKEN = 'okhveeR9k8rCGyLjWrxf8vclQ__B8eSMfOWq1AMm2mEkG8qYkZzTK-xr2X3wh2qI1267yzPq3g_0BLdakcF2CcHwk-oNWm8scFQ7Cvd9Qa_Snlhp1hi0apyBw2f8GoSSPKBgADAZUL'
cache.set('access_token', ACCESS_TOKEN)

print cache.get('access_token')



# pipe = cache.pipeline()
# pipe.set('token_expiration', 3)
# pipe.execute()

print cache.get('token_expiration')