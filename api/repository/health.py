from models.user import User


def check_health():
    health = {
        'text': 'Database health is not ok',
        'working': False
    }
    try:
        users = User.query.limit(1).all()
        health.update({
            'text': 'Database health is ok with {}'.format(
                'some users' if users else 'no user'),
            'working': True
        })
    except Exception as e:
        print(e)

    return health
