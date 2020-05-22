from flask import current_app as app, jsonify
from sqlalchemy_api_handler import as_dict

from models.tag import Tag


@app.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([as_dict(tag) for tag in tags])
