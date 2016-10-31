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
url = 'http://0.0.0.0:6543/membership_api/member/scan'


json_body = {
	'scene_key': 1571902741,
	'scanner_open_id': 'olBwZt_NW0IBseUIa5fImCCj_dn4',
}


res = requests.post(url, json=json_body)
print res.json()