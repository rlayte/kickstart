from flask import Flask

app = Flask(__name__)
app.config.from_envvar('FLASK_SETTINGS')

from __config_project_module__ import views
