from flask import render_template

from {{ PROJECT_NAME }} import app


@app.route('/')
def index():
    return 'Hello {{ PROJECT_NAME }}'
