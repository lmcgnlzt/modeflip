#coding=utf-8

import logging
import requests
import json
from datetime import datetime
import schedule
import time



APPID = 'wx007c42b9e3f7413d'
APPSECRET = '015cc6487b24128615e2ed395f04de52'


def update_access_token():
	url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(APPID, APPSECRET)
	res = requests.get(url)
	data = json.loads(res.text)
	logging.warning('[%s] Token updated: [%s]', datetime.utcnow(), data['access_token'])


# def update_token_test():
# 	logging.warning('[%s] access token updated', datetime.utcnow())


schedule.every(7100).seconds.do(update_access_token)
while True:
	schedule.run_pending()
	time.sleep(1)