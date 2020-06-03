from flask import current_app as app, jsonify, request
from flask_cors import cross_origin
from sqlalchemy_api_handler import ApiHandler

from models.review import Review
from repository.reviews import reviews_query_from_keywords_chain
from utils.rest import listify


@app.route('/reviews', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_reviews():
    query = Review.query

    keywords_chain = request.args.get('keywords')
    if keywords_chain is not None:
        reviews_query_from_keywords_chain(query, keywords_chain)

    return listify(Review,
                   includes=[
                       {'key': key,
                        'includes': [
                            {
                                'key': 'quotedFromAppearances',
                                'includes': ['quotingContent', 'stance']
                            }
                        ]}
                       for key in ['claim', 'content']] + ['reviewer'],
                   query=query,
                   page=request.args.get('page', 1),
                   paginate=10)
