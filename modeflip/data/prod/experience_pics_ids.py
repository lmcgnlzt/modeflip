

import requests
from modeflip.models.designer import *

did = 3

url = 'http://0.0.0.0:6543/designers/{}'.format(did)

json = requests.get(url).json()
d = Designer(**json)
ec = d.experience_content
pics = ec.pics
images = [p.image for p in pics]
ids = [str(url.split('/')[-1].split('.')[0]) for url in images]

print ids