from pymongo.connection import Connection
from pymongo.replica_set_connection import ReplicaSetConnection
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo import ASCENDING, ReadPreference
from pymongo.errors import OperationFailure, AutoReconnect
from time import sleep
from modeflip.utils.retry import retry


def _get_connection(connection_map, **kwargs):
	script = kwargs.pop('script', False)
	connection_map['read_preference'] = ReadPreference.SECONDARY_PREFERRED
	connection_map.update(kwargs)
	return RetryingConnection(**connection_map)


class MongoManager(object):
	"""
	Lazily initialize mongo connections.
	usage:
		get_database = MongoManager(get_configuration())
		db = get_database('mf_config')

	Example usage of options field:
	{
		'mf_config': {
			'read_preference': ReadPreference.PRIMARY_PREFERRED
		}
	}
	"""
	def __init__(self, config_obj, force_load=False, options=None):
		self.config_obj = config_obj
		self.connections = {}
		self.options = options or {}
		if force_load:
			self.force_load()

	def __call__(self, database_name):
		db_cfg = self.config_obj.DB_CONFIG[database_name]
		try:
			db_conn = self.connections[db_cfg['db_alias']]
		except KeyError:
			options = self.options.get(db_cfg['db_alias'], {})
			db_conn = self.connections[db_cfg['db_alias']] = _get_connection(db_cfg['db_host'], **options)

		return db_conn[db_cfg['db_name']]

	def force_load(self):
		"Create all missing connections"
		aliases = {cfg['db_alias'] for cfg in self.config_obj.DB_CONFIG.itervalues()}
		for alias in aliases:
			connection_params = self.config_obj.DB_ALIAS_MAP[alias]
			options = self.options.get(alias, {})
			self.connections[alias] = _get_connection(connection_params, **options)

def field_iterate(cursor, field):
	keys = field.split('.')
	prekeys = keys[0:-1]
	lastkey = keys[-1]
	for item in cursor:
		if len(prekeys) != 0:
			d = item
			for key in prekeys:
				d = d.get(key, {})
			value = d.get(lastkey, 0)
		else:
			value = item.get(field, 0)
		yield value, item


class RetryingCollection(Collection):
	@retry(AutoReconnect, tries=2)
	def insert(self, *args, **kwargs):
		return Collection.insert(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def update(self, *args, **kwargs):
		return Collection.update(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def remove(self, *args, **kwargs):
		return Collection.remove(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def find_one(self, *args, **kwargs):
		return Collection.find_one(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def find(self, *args, **kwargs):
		return Collection.find(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def save(self, *args, **kwargs):
		return Collection.save(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def find_and_modify(self, *args, **kwargs):
		return Collection.find_and_modify(self, *args, **kwargs)

	@retry(AutoReconnect, tries=2)
	def ensure_index(self, *args, **kwargs):
		return Collection.ensure_index(self, *args, **kwargs)

class RetryingDatabase(Database):
	def __getitem__(self, name):
		return RetryingCollection(self, name)

	def __getattr__(self, name):
		return RetryingCollection(self, name)

class RetryingConnection(Connection):
	def __getitem__(self, name):
		return RetryingDatabase(self, name)

	def __getattr__(self, name):
		return RetryingDatabase(self, name)

def get_database_from_config_obj(config_obj, name, **kwargs):
	db_config = config_obj.DB_CONFIG[name]
	connection_map = db_config['db_host']
	connection = _get_connection(connection_map, **kwargs)
	return connection[db_config['db_name']]

def forever_cursor(database, collection, what_fields=None):
	def tail_minus_f_cursor(c):
		start_count = c.count()
		if what_fields:
			cur = Cursor(c, fields=what_fields, tailable=True, timeout=False).sort('$natural', direction=ASCENDING).skip(start_count)
		else:
			cur = Cursor(c, tailable=True, timeout=False).sort('$natural', direction=ASCENDING).skip(start_count)
		return cur

	c = Collection(database, collection)
	cur = tail_minus_f_cursor(c)
	while True:
		try:
			yield cur.next()
		except StopIteration:
			if not cur.alive:
				cur = tail_minus_f_cursor(c)
			sleep(0.1)
		except AutoReconnect:
			if not cur.alive:
				cur = tail_minus_f_cursor(c)
			sleep(0.1)
		except OperationFailure:
			cur = tail_minus_f_cursor(c)
			sleep(0.1)

def batch_insert(db_collection, list_to_add, batch_size):
	count = 0
	insertables_list = []
	for insertable in list_to_add:
		count += 1
		insertables_list.append(insertable)
		if (count % batch_size == 0):
			db_collection.insert(insertables_list)
			insertables_list = []
	if insertables_list:
		db_collection.insert(insertables_list)
