# pylint: disable=R0903

from enum import Enum

from flask.json import JSONEncoder


class EnumJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, Enum):
                return str(obj)
            iterable = [
                {
                    'key': '.'.join(str(element).split('.')[1:]),
                    'value': element.value
                }
                for element in obj
            ]
        except TypeError:
            pass
        else:
            return iterable
        return JSONEncoder.default(self, obj)
