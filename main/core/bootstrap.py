
import sanic

app = sanic.Sanic('test')

from main import views
from main import db