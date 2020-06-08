from flask import current_app as app, jsonify

from repository.health import check_database_health


@app.route('/health', methods=['GET'])
def get_health():
    *TBW*
