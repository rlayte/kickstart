from flask import render_termplate
from __config_project_module__ import app


@app.route('/')
def index():
    return 'Hello {{ PROJECT_NAME }}'
