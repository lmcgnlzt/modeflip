from modeflip.utils.config import get_configuration
from modeflip.utils.redisdb import RedisManager


local_config = get_configuration()
get_cache = RedisManager(local_config, force_load=True)
cache = get_cache('mf_cache')
print cache
print 'access_token: [%s]'%cache.get('access_token')
print 'expires_in: [%s]'%cache.get('expires_in')

