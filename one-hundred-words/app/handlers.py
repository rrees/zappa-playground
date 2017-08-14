
import flask

from flask import render_template

def index():
    return render_template('index.html')

def content_form():
	return flask.redirect(flask.url_for('index'))