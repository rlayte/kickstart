from flask import render_template

from {{ PROJECT }} import app


@app.route('/')
def index():
    return 'Hello {{ PROJECT }}'
