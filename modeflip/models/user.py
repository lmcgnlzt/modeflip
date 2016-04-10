from modeflip.valid_model import Object, ValidationError
from modeflip.valid_model.descriptors import String, Bool, Bool, List, Dict, EmbeddedObject


class User(Object):
	iid = String(nullable=False)
	name = String(nullable=False)
	active = Bool(default=False)


class UserConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['users']