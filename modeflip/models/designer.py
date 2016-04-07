from modeflip.valid_model import Object, ValidationError
from modeflip.valid_model.descriptors import String, Bool


class Designer(Object):
	iid = String(nullable=False)
	name = String(nullable=False, validator=lambda x: x and len(x) >0)


class DesignerConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['designers']
