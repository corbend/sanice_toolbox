
import peewee
from main.core.models import BaseModel


class Event(BaseModel):

	type = peewee.IntegerField(default=1)

	class Meta(object):

		db_table = 'events'