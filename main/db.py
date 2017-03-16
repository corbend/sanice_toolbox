
from main.events.models import Event
from main.core.models import db

models = [
	Event
]

db.connect()
db.create_tables(models, True)



