from datetime import datetime, timedelta

from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *
from modeflip.models.collection import *
from modeflip.models.garment import *
from modeflip.models.transaction import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)
config_db = get_database('mf_config')

dc = DesignerConfig(config_db)
cc = CollectionConfig(config_db)
gc = GarmentConfig(config_db)
tc = TransactionConfig(config_db)





g1 = gc.get(1, 2, 3)
g2 = gc.get(1, 2, 4)
g3 = gc.get(1, 2, 5)
g4 = gc.get(1, 2, 6)


# t1 = Transaction(
# 		tid=tc.get_next_available_id(),
# 		merchant_name='tianjin',
# 		open_id='111',
# 		trans_date=datetime(2016, 10, 10, 15, 16, 20),
# 		trans_points=10,
# 		garments=[g1]
# 		)

# print t1

# tc.set(t1)


# t2 = Transaction(
# 		tid=tc.get_next_available_id(),
# 		merchant_name='tianjin',
# 		open_id='111',
# 		trans_date=datetime(2016, 10, 11, 11, 16, 20),
# 		trans_points=20,
# 		garments=[g2]
# 		)

# print t2

# tc.set(t2)



# t3 = Transaction(
# 		tid=tc.get_next_available_id(),
# 		merchant_name='tianjin',
# 		open_id='222',
# 		trans_date=datetime(2016, 10, 10, 15, 16, 20),
# 		trans_points=30,
# 		garments=[g1]
# 		)

# print t3

# tc.set(t3)



# t4 = Transaction(
# 		tid=tc.get_next_available_id(),
# 		merchant_name='tianjin',
# 		open_id='111',
# 		trans_date=datetime(2016, 10, 12, 7, 11, 20),
# 		trans_points=40,
# 		garments=[g3]
# 		)

# print t4

# tc.set(t4)

"""
print tc.get_all_ids()


start_date = datetime(2016, 10, 9)
end_date = datetime(2016, 10, 12, 7, 11, 21)
# end_date = datetime.now()

print start_date, end_date

# print [t.trans_date for t in tc.get_all_by_merchant_name_within('tianjin', start_date, end_date)]
print [t.trans_date for t in tc.get_all_by_open_id_within('222', start_date, end_date)]
"""

print g3.price, '????'

# g3.price = 826
# t5 = Transaction(
# 		tid=tc.get_next_available_id(),
# 		merchant_name='tianjin',
# 		open_id='111',
# 		trans_date=datetime(2016, 10, 13, 13, 14, 20),
# 		trans_points=50,
# 		garments=[g3]
# 		)

# print t5

# tc.set(t5)