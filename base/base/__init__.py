from flask import Flask

app = Flask(__name__)

import {{ PROJECT_NAME }}.views
