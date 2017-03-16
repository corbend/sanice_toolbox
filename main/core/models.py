
import peewee
from playhouse.shortcuts import model_to_dict
#from playhouse.pool import PooledPostgresqlDatabase

db = peewee.PostgresqlDatabase(
    'globl',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='postgres',  # Ditto.
    host='localhost',  # Ditto.
    # max_connections=8,
    # stale_timeout=300
)

class BaseModel(peewee.Model):

	id = peewee.BigIntegerField()
	created = peewee.DateTimeField()	

	class Meta(object):
		database = db

	def to_json(self):
		return model_to_dict(self)





