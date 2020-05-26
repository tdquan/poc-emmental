from flask import current_app as app, jsonify

from repository.health import check_health


@app.route('/health', methods=['GET'])
def get_health():
    return jsonify({'json': '{name} *TBW* {app_path}'.format(name=__name__, app_path=app.root_path)})
