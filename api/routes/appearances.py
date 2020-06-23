# pylint: disable=W0212

from flask import current_app as app, jsonify, request
from flask_login import current_user, login_required
from sqlalchemy_api_handler import ApiHandler, \
                                   as_dict, \
                                   humanize

from models.appearance import Appearance, StanceType
from models.content import Content


@app.route('/appearances', methods=['POST'])
@login_required
def post_appearance():

    content = Content.create_or_modify({'url': request.json['url']}, search_by='url')

    appearance = Appearance(
        quotedClaimId=*TBW*,
        quotingContent=content,
        stance=getattr(StanceType, *TBW*),
        testifier=current_user._get_current_object()
    )

    ApiHandler.save(appearance)

    return jsonify(as_dict(appearance, includes=['quotingContent'])), 201
