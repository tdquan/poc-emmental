from flask import Flask, current_app as app

from utils.setup import setup
from utils.db import db
from models.user import User


FLASK_APP = Flask(__name__)


@FLASK_APP.shell_context_processor
def make_shell_context():
  return({'app': app, 'db': db, 'User': User})


setup(FLASK_APP)
