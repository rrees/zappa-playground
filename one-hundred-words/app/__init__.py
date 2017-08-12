
from flask import Flask

from . import handlers

app = Flask(__name__)

routes = [
	('/', 'index', handlers.index, ['GET', 'POST']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)
