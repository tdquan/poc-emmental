from flask import Flask

from utils.setup import setup


FLASK_APP = Flask(__name__)


setup(FLASK_APP,
      with_models_creation=True,
      with_routes=True)


if __name__ == '__main__':
    FLASK_APP.run()
