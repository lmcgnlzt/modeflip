#coding=utf-8

import logging
import requests
import json
from datetime import datetime
import schedule
import time
from modeflip.utils.config import get_configuration
from modeflip.utils.redisdb import RedisManager


local_config = get_configuration()
get_cache = RedisManager(local_config, force_load=True)
cache = get_cache('mf_cache')


APPID = 'wx007c42b9e3f7413d'
APPSECRET = '015cc6487b24128615e2ed395f04de52'


def update_access_token():
	url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(APPID, APPSECRET)
	res = requests.get(url)
	data = json.loads(res.text)
	access_token = data['access_token']
	expires_in = data['expires_in']
	pipe = cache.pipeline()
	pipe.set('access_token', access_token)
	pipe.set('expires_in', expires_in)
	pipe.execute()
	logging.warning('[%s] Token updated: [%s], expires_in: [%s]', datetime.utcnow(), access_token, expires_in)


# def update_token_test():
# 	logging.warning('[%s] access token updated', datetime.utcnow())


schedule.every(7100).seconds.do(update_access_token)
while True:
	schedule.run_pending()
	time.sleep(1)