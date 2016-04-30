from modeflip.valid_model.exc import ValidationError
from modeflip.valid_model.base import Object
from modeflip.valid_model.descriptors import Generic, EmbeddedObject as _EmbeddedObject, Dict as _Dict, Set as _Set, DateTime as _DateTime, TimeDelta as _TimeDelta, Float as _Float, Integer as _Integer, String
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from collections import Mapping
import re
# from cassandra.util import sortedset

def is_descriptor(obj):
	return all((
		hasattr(obj, 'name'),
		hasattr(obj, '__delete__'),
		hasattr(obj, '__get__'),
		hasattr(obj, '__set__')
	))

def get_filtered_model_list(model_list, included_keys):
	return [{k: getattr(d, k) for k in included_keys} for d in model_list]

def not_none(value):
	return value is not None

def keys_are_type(allowed_types):
	def inner(value):
		return all(isinstance(i, allowed_types) for i in value)
	return inner

def values_are_type(allowed_types):
	def inner(value):
		return all(isinstance(i, allowed_types) for i in value.itervalues())
	return inner

def keys_and_values_are_types(allowed_key_types, allowed_value_types):
	def inner(value):
		for k, v in value.iteritems():
			if not isinstance(k, allowed_key_types):
				return False
			if not isinstance(v, allowed_value_types):
				return False
		return True
	return inner

class Serialized(Generic):
	def __init__(self, value, serialize, deserialize):
		assert isinstance(value, Generic)
		self.value = value
		self.serialize = serialize
		self.deserialize = deserialize
		Generic.__init__(self, default=None)
	def __get__(self, instance, klass=None):
		result = Generic.__get__(self, instance, klass=klass)
		if result is not None and result is not self:
			dummy = Object()
			result = self.deserialize(result)
			result = self.value.__set__(dummy, result)
		return result
	def __set__(self, instance, value):
		if isinstance(value, basestring):
			value = self.deserialize(value)
		dummy = Object()
		value = self.value.__set__(dummy, value)
		if value is not None:
			value = self.serialize(value)
		return Generic.__set__(self, instance, value)

class MongoObjectId(Generic):
	def __init__(self, default=None, validator=None, mutator=None):
		Generic.__init__(
			self, default=default, validator=validator, mutator=mutator
		)

	def __set__(self, instance, value):
		if value is not None and not isinstance(value, ObjectId):
			raise ValidationError("{!r} is not an ObjectId".format(value))
		return Generic.__set__(self, instance, value)

class Integer(_Integer):
	def __set__(self, instance, value):
		if isinstance(value, (basestring, long)):
			print '??????'
			try:
				value = int(value)
			except ValueError:
				raise ValidationError("{!r} could not be converted to an integer".format(value))
		return _Integer.__set__(self, instance, value)

class Float(_Float):
	def __set__(self, instance, value):
		if isinstance(value, basestring):
			try:
				value = float(value)
			except ValueError:
				raise ValidationError("{!r} could not be converted to a float".format(value))
		return _Float.__set__(self, instance, value)

class DateTime(_DateTime):
	def __set__(self, instance, value):
		if isinstance(value, (float, int)):
			try:
				value = datetime.utcfromtimestamp(value)
			except ValueError:
				raise ValidationError("{!r} could not be converted to a datetime".format(value))
		elif isinstance(value, basestring):
			try:
				value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
			except ValueError:
				raise ValidationError("{!r} could not be converted to a datetime".format(value))
		return _DateTime.__set__(self, instance, value)

class TimeDelta(_TimeDelta):
	def __set__(self, instance, value):
		if isinstance(value, (float, int)):
			try:
				value = timedelta(seconds=value)
			except (TypeError, ValueError):
				raise ValidationError("{!r} could not be converted to a timedelta".format(value))
		return _TimeDelta.__set__(self, instance, value)

class PlainText(String):
	def __set__(self, instance, value):
		if isinstance(value, basestring):
			value = BeautifulSoup(value).get_text(strip=True)
		return String.__set__(self, instance, value)

class Regex(String):
	def __set__(self, instance, value):
		if isinstance(value, basestring):
			try:
				re.compile(value)
			except re.error:
				raise ValidationError("{!r} invalid regular expression".format(value))
		return String.__set__(self, instance, value)

def examine_schema(collection, field=None):
	from collections import defaultdict
	from pprint import pprint
	t = defaultdict(lambda:defaultdict(int))
	for doc in collection.find():
		if field and isinstance(doc.get(field), dict):
			for k, v in doc.get(field, {}).iteritems():
				t[k][type(v)] += 1
		elif field and isinstance(doc.get(field), list):
			for subdoc in doc.get(field, []):
				for k, v in subdoc.iteritems():
					t[k][type(v)] += 1
		elif not field:
			for k, v in doc.iteritems():
				t[k][type(v)] += 1
	pprint(dict(t))

def dd_examine_schema(collection, field1, field2, print_=False):
	from collections import defaultdict
	from pprint import pprint
	t = defaultdict(lambda:defaultdict(int))
	for doc in collection.find():
		for k, v in doc.get(field1, {}).get(field2, {}).iteritems():
			if print_:
				print v
			t[k][type(v)] += 1
	pprint(dict(t))

def ddl_examine_schema(collection, field1, field2, print_=False):
	from collections import defaultdict
	from pprint import pprint
	t = defaultdict(lambda:defaultdict(int))
	for doc in collection.find():
		for subdoc in doc.get(field1, []):
			if isinstance(subdoc.get(field2), dict):
				for k, v in subdoc.get(field2, {}).iteritems():
					if print_:
						print v
					t[k][type(v)] += 1
	pprint(dict(t))

# class EmbeddedObject(_EmbeddedObject):
# 	'''
# 	Customized EmbeddedObject Descriptor inherited from ValidModel EmbeddedObject.
# 	'''
# 	def __set__(self, instance, value):
# 		if isinstance(value, Mapping):
# 			value = self.class_obj(**value)
# 		return _EmbeddedObject.__set__(self, instance, value)

# class Dict(_Dict):
# 	'''
# 	Customized Dict Descriptor inherited from ValidModel Dict.
# 	'''
# 	def __set__(self, instance, value):
# 		if not isinstance(value, dict) and isinstance(value, Mapping): # limit the casting scope, avoid converting OrderedDict
# 			value = dict(value)
# 		return _Dict.__set__(self, instance, value)

# class Set(_Set):
# 	'''
# 	Customized Set Descriptor inherited from ValidModel Set.
# 	'''
# 	def __set__(self, instance, value):
# 		if isinstance(value, sortedset):
# 			value = set(value)
# 		return _Set.__set__(self, instance, value)

# if __name__ == '__main__':
# 	import sys
# 	from vr.common.config import get_configuration
# 	from vr.common.utils import mongo

# 	config = get_configuration()
# 	config_db = mongo.get_database_from_config_obj(config, 'vr_config')
# 	examine_schema(config_db[sys.argv[1]])
