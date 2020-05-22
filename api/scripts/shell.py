from flask import Flask

from utils.setup import setup


FLASK_APP = Flask(__name__)

setup(FLASK_APP)
