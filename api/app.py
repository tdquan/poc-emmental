from flask import Flask

from utils.setup import setup


FLASK_APP = Flask(__name__)


setup(FLASK_APP,
      with_cors=True,
      with_models_creation=True,
      with_routes=True)


if __name__ == '__main__':
    FLASK_APP.run(
        debug=(FLASK_APP.config.get('ENV') == 'development' or 'test'),
        host=FLASK_APP.config.get('HOST', '0.0.0.0'),
        port=FLASK_APP.config.get('PORT', 5000)
    )
