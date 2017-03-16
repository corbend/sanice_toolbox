
from main.core.bootstrap import app
from sanic.response import json
from main.events.models import Event
import pendulum
#from main.views import events_bp
from main.core.bootstrap import app

print("event views")

@app.route('/events', methods=['GET'])
async def get_events(request):
	
	events = Event.select()
	print(events)

	return json({"rows": map(Event.to_json, events)})


@app.route('/events/save', methods=['GET'])
async def save_events(request):
	
	event = Event(id=2, created=pendulum.Pendulum.now(), type=request.form.get('type'))
	print(event)
	event.save()

	return json({"item": event.to_json()})