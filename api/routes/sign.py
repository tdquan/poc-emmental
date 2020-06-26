from flask_login import current_user, \
                        login_required, \
                        logout_user, \
                        login_user
from flask import current_app as app, jsonify, request
from flask_cors import cross_origin
from sqlalchemy_api_handler import ApiHandler, as_dict

from repository.login_manager import stamp_session, discard_session
from repository.users import get_user_with_credentials


INCLUDES = [
    '-password'
]


@app.route('/users/current', methods=['GET'])
@login_required
def get_current_user():
    return jsonify(as_dict(current_user, includes=INCLUDES))


@app.route('/users/signin', methods=['POST'])
@app.route('/signin', methods=['POST'])
@cross_origin(supports_credentials=True)
def signin():
    json = request.get_json()
    identifier = json.get('identifier')
    password = json.get('password')
    user = get_user_with_credentials(identifier, password)
    login_user(user, remember=True)
    stamp_session(user)
    return jsonify(as_dict(user, includes=INCLUDES)), 200


@app.route('/users/signout', methods=['GET'])
@login_required
def signout():
    discard_session()
    logout_user()
    return jsonify({'global': 'Disconnected'})
