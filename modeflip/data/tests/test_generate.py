import json
import requests


from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.models.item import *
from pprint import pprint


local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

ic = ItemConfig(config_db)
url = 'http://0.0.0.0:6543/merchant/generate'


item = ic.get_by_tag('17BHC201005')
item.price = 811
merchant_name = 'tianjin'
items = [item.__json__()]

json_body = {
	'merchant_name': merchant_name,
	'items': items,
}


res = requests.post(url, json=json_body)
print res