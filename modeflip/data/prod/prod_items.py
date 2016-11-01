#coding=utf-8

import sys
import xlrd
import pandas as pd
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
from modeflip.models.item import Item


from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.models.item import *


local_config = get_configuration('production')
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')
ic = ItemConfig(config_db)

def import_items(file_name):
	LOCAL_FILE = file_name
	df = pd.read_excel(LOCAL_FILE, encoding=sys.getfilesystemencoding())

	data = df.ix[:, 2:12].dropna(how='all') # remove all rows whose values are all nan
	data = data.where((pd.notnull(data)), None) # replace all nan with None
	print data


	INDEXES = list(range(3, 10))
	SIZES = ('XS', 'S', 'M', 'L', 'XL', 'F', 'F+')
	index_size_mapping = dict(zip(INDEXES, SIZES))



	for index, row in data.iterrows():
		item = Item(
			tag=str(int(row[0])),
			name=row[1].encode('utf-8'),
			original_price=float(int(row[2])),
			available_sizes=[index_size_mapping[i] for i in range(3, 10) if row[i] is not None],
			)
		ic.set(item)
		print item.tag, item.name, item.original_price, item.available_sizes


	# print ic.get_by_tag('171010101')
	# print ic.get_all_tags()



if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: python prod_items.py file_name'
		sys.exit(1)

	file_name = sys.argv[1]
	import_items(file_name)