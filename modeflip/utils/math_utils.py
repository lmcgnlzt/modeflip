from random import choice
import string

def relative_percentage(x, y):
	if x == 0 and y == 0:
		return 0, 0
	s = x + y
	return (x * 100.0)/s, (y * 100.0)/s

def relative_percentage_dict(d):
	sum = reduce(lambda x,y: x+y, d.values(), 0)
	if sum == 0:
		return d
	rel_dict = dict(
		(item, (d[item]*100.0)/sum)
		for item in d
	)
	return rel_dict

def format(s, tSep=",", dSep='.', zeros=2):
	if s == None:
		return 0
	if isinstance(s, int) or isinstance(s,long) or isinstance(s,float):
		s = str(s)
	if s.rfind('.')>0:
		rhs=s[s.rfind('.')+1:]
		if len(rhs) > 0:
			if len(rhs) < zeros:
				rhs = rhs.ljust(zeros, '0')
			else:
				rhs = rhs[:zeros]
		s=s[:s.rfind('.')]
		if len(s) <= 3 or (len(s) == 4 and s[0] == '-'):
			ret = s + dSep + rhs if rhs else s
			return ret

		lhs = format(s[:-3], tSep) + tSep + s[-3:]

		return lhs + dSep + rhs if rhs else lhs
	else:
		if len(s) <= 3 or (len(s) == 4 and s[0] == '-'):
			return s

		return format(s[:-3], tSep) + tSep + s[-3:]

def get_ctr_min_max_limit(ctr_list, std_multiple=1.28):
	import numpy
	#std_multiple of 1.28 = 80% confidence level
	ctr_avg = numpy.average(ctr_list) #@UndefinedVariable
	ctr_std = numpy.std(ctr_list) #@UndefinedVariable
	min_limit = ctr_avg - std_multiple * ctr_std
	max_limit = ctr_avg + std_multiple * ctr_std
	if min_limit < 0:
		min_limit = 0

	return (min_limit, max_limit)

def currency(num, config, override=None):
	override = override or {}
	from vr.common.utils import math_utils
	from vr.common.utils.url_utils import toutf8

	config.update(override)

	num = math_utils.format(num, config['thousands_separator'], config['decimal_separator'], config['decimal_places'])

	if 'symbol' in config:
		if config['symbol_at_beginning']:
			if 'use_symbol_char' in config:
				num = toutf8(config['symbol_char']) + ' ' + num
			else:
				num = config['symbol'] + ' ' + num
		else:
			if 'use_symbol_char' in config:
				num = num + ' ' + toutf8(config['symbol_char'])
			else:
				num = num + ' ' + config['symbol']

	return num

def get_ctr(clicks, views):
	if clicks is None:
		clicks = 0
	if views is None:
		views = 0
	try:
		ctr = round(float(clicks) / views, 6)
	except ZeroDivisionError:
		ctr = 0
	return ctr

def generate_random_key(length=8, chars=string.letters + string.digits):
	return ''.join([choice(chars) for i in range(length)]).lower()

def roll_window_sum(river, window):
	returnlist = []
	for i in range(0, len(river) - window + 1):
		point_sum = 0
		non_zero_count = 0
		for point in river[i:i + window]:
			if point and point > 0:
				point_sum += point
				non_zero_count += 1
		if non_zero_count > (0.25 * window):
			point_sum = point_sum * window / non_zero_count
		else:
			point_sum = 0
		returnlist.append(point_sum)
	return returnlist
