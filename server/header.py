import os
from flask import Flask

#  SETTING DEFAULT TEMPLATES PATH
DEFAULT_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../src/"))


app = Flask(__name__, template_folder=DEFAULT_PATH, static_folder=DEFAULT_PATH)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
