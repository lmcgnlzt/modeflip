from redis import StrictRedis


def _get_connection(db_config):
	db_type = db_config['db_type']
	if db_type == 'standalone':
		host = db_config['host']
		port = db_config['port']
		db = db_config.get('db', 0)
		return StrictRedis(host=host, port=port, db=db)


def from_key(local_config, db_name):
	return _get_connection(local_config.REDIS[db_name])


class RedisManager(object):

	"""
	Lazily initialize redis connections.
	usage:
		get_cache = RedisManager(get_configuration())
		cache = get_cache('main')
	"""

	def __init__(self, config, force_load=False):
		self.config = config
		self.connections = {}
		if force_load:
			self.force_load()

	def __call__(self, db_name):
		try:
			db_conn = self.connections[db_name]
		except KeyError:
			db_conn = from_key(self.config, db_name)
			self.connections[db_name] = db_conn
		return db_conn

	def force_load(self):
		for db_name in self.config.REDIS:
			self.connections[db_name] = from_key(self.config, db_name)