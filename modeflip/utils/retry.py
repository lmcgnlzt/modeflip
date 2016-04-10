import time
import logging

log = logging.getLogger(__name__)

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
	"""Retry decorator
	original from http://wiki.python.org/moin/PythonDecoratorLibrary#Retry
	"""
	def deco_retry(f):
		def f_retry(*args, **kwargs):
			mtries, mdelay = tries, delay
			try_one_last_time = True
			while mtries > 1:
				try:
					return f(*args, **kwargs)
				except ExceptionToCheck, e:
					log.error("%s, Retrying in %d seconds...", str(e), mdelay)
					time.sleep(mdelay)
					mtries -= 1
					mdelay *= backoff
			if try_one_last_time:
				return f(*args, **kwargs)
			return
		return f_retry # true decorator
	return deco_retry
