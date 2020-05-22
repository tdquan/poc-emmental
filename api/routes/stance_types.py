from flask import current_app as app, jsonify

from models.appearance import StanceType


@app.route('/stanceTypes', methods=['GET'])
def get_stance_types():
    return jsonify(StanceType)
