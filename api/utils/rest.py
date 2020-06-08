from flask import jsonify
from sqlalchemy_api_handler import get_result


def listify(*args, **kwargs):
    result = get_result(*args, **kwargs)

    response = jsonify(result['data'])

    if 'total_data_count' in result:
        response.headers['Total-Data-Count'] = result['total_data_count']
        response.headers['Access-Control-Expose-Headers'] = 'Total-Data-Count'
        if 'has_more' in result:
            response.headers['Has-More'] = result['has_more']
            response.headers['Access-Control-Expose-Headers'] += ',Has-More'

    return response
