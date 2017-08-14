
import flask

from . import handlers

app = flask.Flask(__name__)

routes = [
	('/', 'index', handlers.index, ['GET']),
	('/forms/content', 'post_content', handlers.content_form, ['POST'])
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)
