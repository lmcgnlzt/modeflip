#coding=utf-8

import logging
import requests
import json
from datetime import datetime
import schedule
import time


LOGGER = logging.getLogger(__name__)


APPID = 'wx007c42b9e3f7413d'
APPSECRET = '015cc6487b24128615e2ed395f04de52'


def update_access_token():
	url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(APPID, APPSECRET)
	res = requests.get(url)
	data = json.loads(res.text)
	print data['access_token']


def update_token_test():
	LOGGER.warning('[%s] access token updated', datetime.utcnow())


schedule.every(5).seconds.do(update_token_test)
while True:
	schedule.run_pending()
	time.sleep(1)