
import datetime
import pendulum

from typing import List
from app import conf

stz = conf['server']['tz']


FORMATS = [
	'DD.MM.YYYY HH:mm:ss',
	'DD.MM.YYYY'
]


def _try_formats(dt_str:str, formats:List[str]=FORMATS) -> datetime.datetime:
	dt_parsed = None
	for fmt in formats:
		try:
			dt_parsed = pendulum.from_format(dt_str, fmt, tz=stz)
			return dt_parsed
		except Exception:
			continue
	return None 


def parse_datetime(dt_str:str, fmt:str=None) -> datetime.datetime:

	dt_parsed = None

	if dt_str is None:
		return None

	if fmt is None:
		dt_parsed = pendulum.parse(dt_str, tz=stz)

		if dt_parsed:
			return dt_parsed
		else:
			_try_formats(dt_str)
