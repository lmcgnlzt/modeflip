from modeflip.valid_model import Object
from modeflip.valid_model.descriptors import String, List, EmbeddedObject


class ProfileImages(Object):
	icon_url = String(validator=lambda x: '/' in x)
	image_url = String(validator=lambda x: '/' in x)
	background_url = String(validator=lambda x: '/' in x)


class Picture(Object):
	title = String(default='')
	thumbnail = String(validator=lambda x: '/' in x)
	image = String(validator=lambda x: '/' in x)


class Video(Object):
	title = String(default='')
	thumbnail = String(validator=lambda x: '/' in x) # with play button
	poster = String(validator=lambda x: '/' in x) # without play button
	url = String(validator=lambda x: '/' in x)


class Music(Object):
	title = String(default='')
	thumbnail = String(validator=lambda x: '/' in x)
	url = String(validator=lambda x: '/' in x)


class PicturePage(Object):
	pics = List(value=EmbeddedObject(Picture))