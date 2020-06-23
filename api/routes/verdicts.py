from flask import current_app as app, jsonify, request
from sqlalchemy_api_handler import ApiHandler

from models.verdict import Verdict
from repository.reviews import keep_verdicts_with_keywords_chain, \
                               keep_verdicts_with_tag
from utils.rest import listify


INCLUDES = [
    {
        'key': key,
        'includes': [
            {
                'key': 'quotedFromAppearances',
                'includes': [
                    {
                        'key': 'quotingContent',
                        'includes': [
                            {
                                'key': 'authorContents',
                                'includes': ['author']
                            },
                            {
                                'key': 'medium',
                                'includes': ['organization']
                            }
                        ]
                    },
                    'stance'
                ]
            }
        ]
    } for key in ['claim', 'content']
] + [
    'editor',
    {
        'key': 'verdictReviewers',
        'includes': [
            {
                'key': 'reviewer',
                'includes': ['review']
            }
        ]
    },
    {
        'key': 'verdictTags',
        'includes': ['tag']
    }
]


@app.route('/verdicts/<verdict_id>', methods=['GET'])
def get_verdict(verdict_id):
    verdict = load_or_404(Verdict, verdict_id)
    return jsonify(*TBW*)
    

@app.route('/verdicts', methods=['GET'])
def get_reviews():
    query = Verdict.query

    keywords_chain = request.args.get('keywords')
    if keywords_chain is not None:
        query = *TBW*

    tag = request.args.get('tag')
    if tag:
        query = *TBW*

    return listify(Verdict,
                   includes=INCLUDES,
                   query=query,
                   page=request.args.get('page', 1),
                   paginate=10)
