from flask import render_template
from __config_project_module__ import app


@app.route('/')
def index():
    return 'Hello {{ PROJECT_NAME }}'
