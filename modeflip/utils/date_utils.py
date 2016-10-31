from datetime import datetime, timedelta, tzinfo as tzinfoclass
from pytz import timezone
from copy import deepcopy

def normalize_on_minute(dtstamp, minute):
	"""
	Change a datetime stamp to be rounded down to the nearest interval of `minute`.
	This also truncates off the seconds and microseconds parameters by setting them to 0.

	>>> normalize_on_minute(datetime(2012, 3, 19, 15, 9, 12, 41), 15)
	datetime.datetime(2012, 3, 19, 15, 0)
	>>> normalize_on_minute(datetime(2013,3, 19, 15, 24, 20, 19), 20)
	datetime.datetime(2013, 3, 19, 15, 20)
	"""

	tsmin = dtstamp.minute
	rounded_tsmin = tsmin - (tsmin % minute)
	return dtstamp.replace(microsecond=0, second=0, minute=rounded_tsmin)

def unix_timestamp_int_in_seconds(dt_stamp):
	unix_delta = dt_stamp - datetime(1970, 1, 1)
	return int(unix_delta.total_seconds())

def unix_timestamp(dt_stamp):
	unix_delta = dt_stamp - datetime(1970, 1, 1)
	return unix_delta.total_seconds()

def round_datetime(dt_stamp, delta):
	if isinstance(delta, timedelta):
		delta = int(delta.total_seconds())
	else:
		delta = int(delta)
	return datetime.utcfromtimestamp(unix_timestamp(dt_stamp) * delta // delta)

def unix_timestamp_millis(dt_stamp):
	return int(unix_timestamp(dt_stamp) * 1000)

def unix_timestamp_from_iso_string(iso_string):
	dt = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ")
	return unix_timestamp(dt) * 1000

def this_local_midnight(tz_str):
	tz = create_timezone(tz_str)
	utc = create_timezone('UTC')
	now = utc.localize(datetime.utcnow()).astimezone(tz).replace(hour=0, minute=0, second=0, microsecond=0)
	now += timedelta(days=1)
	return now.astimezone(utc).replace(tzinfo=None)

def last_local_midnight(tz_str):
	tz = create_timezone(tz_str)
	utc = create_timezone('UTC')
	now = utc.localize(datetime.utcnow()).astimezone(tz).replace(hour=0, minute=0, second=0, microsecond=0)
	return now.astimezone(utc).replace(tzinfo=None)

def local_date(dtstamp, tz_str):
	tz = create_timezone(tz_str)
	utc = create_timezone('UTC')
	return utc.localize(dtstamp).astimezone(tz).date()

def getNow(tz=None):
	if tz is None:
		tz = create_timezone('UTC')
	else:
		tz = create_timezone(tz)
	utc = create_timezone('UTC')
	now = utc.localize(datetime.utcnow()).astimezone(tz).replace(microsecond=0, tzinfo=None)
	return now

def create_timezone(tz):
	if tz is None:
		tz = timezone('UTC')
	elif isinstance(tz, tzinfoclass):
		tz = tz
	else:
		tz = timezone(tz)
	return tz

def convert_tz1_to_tz2(time, tz1, tz2):
	"Convert naive time from tz1 to tz2"
	tz1 = create_timezone(tz1)
	tz2 = create_timezone(tz2)
	return tz1.localize(time).astimezone(tz2).replace(tzinfo=None)

def tzInUtc(time, tz_str=None):
	"Convert from `tz_str` to UTC"
	if tz_str is None or tz_str == 'UTC':
		return time
	delta = getNow('UTC') - getNow(tz_str)
	return time + delta

def utcInTz(time, tz_str=None):
	"Convert from UTC to `tz_str`"
	if tz_str == None or tz_str == 'UTC':
		return time
	delta = getNow("UTC") - getNow(tz_str)
	return time - delta

def formatTimedelta(t):
	days = t.days
	hours = t.seconds / 3600
	remaining_seconds = t.seconds
	remaining_seconds = remaining_seconds - hours * 3600
	minutes = remaining_seconds / 60
	seconds = remaining_seconds - minutes * 60
	output = ''
	if days > 0:
		hours += days * 24
	prefix = ''
	if hours >= 1:
		output += prefix + str(hours) + 'h '
	prefix = ''
	if minutes < 10:
		prefix = '0'
	output += prefix + str(minutes) + 'm '
	prefix = ''
	if seconds < 10:
		prefix = '0'
	output += prefix + str(seconds) + 's'
	return output

def formatFriendlyTimedelta(t):
	"""
	Same as formatTimedelta; didn't want to affect other code using this function
	Added check to return time in days in case # hours is > 95
	"""
	days = t.days
	hours = t.seconds / 3600
	remaining_seconds = t.seconds
	remaining_seconds = remaining_seconds - hours * 3600
	minutes = remaining_seconds / 60
	output = ''
	if days > 0:
		hours += days * 24
	prefix = ''
	if hours >= 95:
		output = int(round(days + (hours / 24.0)))
		return str(output) + ' days'
	if hours >= 1:
		output += prefix + str(hours) + 'h '
	prefix = ''
	if minutes < 10:
		prefix = '0'
	output += prefix + str(minutes) + 'm '
	# no seconds for this time format
	return output

def getRangeOfArbitraryDate(time, tz_str):
	day_start_in_tz = datetime(time.year, time.month, time.day)
	day_start_in_utc = tzInUtc(day_start_in_tz, tz_str)
	return {'b': day_start_in_utc, 'e': day_start_in_utc + timedelta(hours=24)}

def getRangeOfWorkingHoursDate(time, tz_str, working_hours=None):
	day_of_week = time.strftime('%A')
	if working_hours:
		if working_hours[day_of_week]['is_working_day']:
			info = working_hours[day_of_week]
			starting_hour = int(info['starting_hour'])/100
			ending_hour = int(info['ending_hour'])/100
			day_start_in_tz = datetime(time.year, time.month, time.day, starting_hour)
			try:
				day_end_in_tz = datetime(time.year, time.month, time.day, ending_hour)
			except ValueError:
				day_end_in_tz = datetime(time.year, time.month, time.day, 23)
			return {'b': tzInUtc(day_start_in_tz, tz_str), 'e': tzInUtc(day_end_in_tz, tz_str)}
		else:
			return {}
	else:
		return getRangeOfArbitraryDate(time, tz_str)

def formatTimedeltaToSeconds(t):
	return (t.days * 86400) + t.seconds

def getTodayBeginning(tz_str='UTC'):
	utc = create_timezone('UTC')
	tz = create_timezone(tz_str)
	now = utc.localize(datetime.utcnow()).astimezone(tz).replace(hour=0, minute=0, second=0, microsecond=0).astimezone(utc).replace(tzinfo=None)
	return now

def getNumberOfDaysBetween(d1, d2, tz_str='UTC'):
	""" d1 and d2  are datetime objects in UTC """
	d1_date = utcInTz(d1, tz_str)
	d2_date = utcInTz(d2, tz_str)
	d1_date = deepcopy(d1_date).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
	d2_date = deepcopy(d2_date).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
	return abs((d1_date - d2_date).days)

def getLast7DaysRange(tz_str='UTC'):
	todayBeginning = getTodayBeginning(tz_str)
	return {'b': todayBeginning - timedelta(days=7), 'e': todayBeginning}

def getLast14DaysRange(tz_str='UTC'):
	todayBeginning = getTodayBeginning(tz_str)
	return {'b': todayBeginning - timedelta(days=14), 'e': todayBeginning}

def ordinal(n):
	if 10 <= n % 100 < 20:
		return str(n) + 'th'
	else:
		return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")