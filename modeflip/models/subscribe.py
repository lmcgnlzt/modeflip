from modeflip.valid_model import Object, ValidationError
from modeflip.valid_model.descriptors import String, Bool, Bool, List, Dict, EmbeddedObject
from modeflip.models.user import User
from modeflip.models.designer import Designer


class Subscribe(Object):
	user = User(nullable=False)
	designer = Designer(nullable=False)


class SubscribeConfig(object):

	def __init__(self, database):
		self.database = database
		self.collection = database['subscribes']