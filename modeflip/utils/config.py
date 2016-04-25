import os
import re
import socket
import yaml

MODE_VARIABLE = 'CONFIGURATION'
MODE_DEFAULT = 'development'
PATH_VARIABLE = 'CONFIG_PATH'
PATH_DEFAULT = '~/modeflip/modeflip'

class HostInfo(object):
	HOST_REGEX = re.compile(r'^(?P<name>\w+)-(?P<number>\d+)-(?P<env>\w+)-(?P<dc>\w+)$')

	def __init__(self, hostname=None):
		_hostname = hostname or socket.gethostname()
		self.host = _hostname.split('.')[0]
		m = self.HOST_REGEX.match(self.host)
		if not m and is_production_environment():
			raise RuntimeError('Could not parse info from host: {!r}'.format(self.host))
		else:
			self.name = m.group('name') if m else None
			self.number = m.group('number') if m else None
			self.environment = m.group('env') if m else None
			self.datacenter = m.group('dc') if m else None

class ConfigObj(object):
	def __init__(self, config_dict):
		self._config = config_dict
		self._host_info = None

	def __getitem__(self, key):
		return self._config[key]

	def __getattr__(self, key):
		try:
			return self._config[key]
		except KeyError:
			raise AttributeError(key)

	def __delattr__(self, key):
		if key.startswith('_'):
			raise RuntimeError('Don\'t delete private variables')
		try:
			del self._config[key]
		except KeyError:
			raise AttributeError(key)

	def __json__(self):
		config_data = {
			'DATACENTER': self.DATACENTER,
			'ENV_SHORT_NAME': self.ENV_SHORT_NAME,
		}
		config_data.update(self._config)
		return config_data

	def to_yaml(self):
		return yaml.dump(self._config)

	@property
	def DATACENTER(self):
		return self.host_info.datacenter or self._config['DATACENTER']

	@property
	def ENV_SHORT_NAME(self):
		return self.host_info.environment or self._config['ENV_SHORT_NAME']

	@property
	def host_info(self):
		if not self._host_info:
			self._host_info = HostInfo()
		return self._host_info

def get_current_configuration():
	return os.environ.get(MODE_VARIABLE, MODE_DEFAULT)

def is_production_environment():
	return get_current_configuration() in ['production', 'datacenter']

def get_configuration(mode=None):
	config_path = os.path.expanduser(os.environ.get(PATH_VARIABLE, PATH_DEFAULT))
	mode = mode or os.environ.get(MODE_VARIABLE, MODE_DEFAULT)
	filepath = os.path.join(config_path, '{}.yaml'.format(mode))
	return get_configuration_from_file(filepath)

def get_configuration_from_file(filepath):
	import logging
	logging.getLogger(__name__).info('Loading configuration file: %s', filepath)

	with open(filepath) as f:
		config_obj = ConfigObj(yaml.load(f))
	return config_obj