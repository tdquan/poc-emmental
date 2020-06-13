# pylint: disable=C0415
# pylint: disable=W0611

from os import walk
from os.path import abspath, basename, dirname, join
from importlib import import_module
from sys import modules
from sqlalchemy_api_handler import logger

from utils.db import db, Model
from repository.keywords import import_keywords

PROJ_DIR = abspath(join(dirname(abspath(__file__)), '../'))
APP_MODULE = basename(PROJ_DIR)

__all__ = []


def get_modules():
    """Returns all .py modules in given file_dir that are not __init__."""
    file_dir = abspath(join(PROJ_DIR, 'models'))
    for root, dirnames, files in walk(file_dir):
        mod_path = '{path}'.format(path=root.split(PROJ_DIR)[1][1:]).replace('/', '.')
        for filename in files:
            if filename.endswith('.py') and not filename.startswith('__init__') and 'mixin' not in filename:
                yield '.'.join([mod_path, filename[0:-3]])


def dynamic_loader():
    items = []
    for mod in get_modules():
        module = import_module(mod)
        if hasattr(module, '__model__'):
            item = getattr(module, module.__model__)
            items += [item] if issubclass(item, Model) else False
    return items


def import_models(with_creation=False):
    for model in dynamic_loader():
        logger.info('importing {model}...'.format(model=model.__name__))
        setattr(modules[__name__], model.__name__, model)
        __all__.append(model)

    if with_creation:
        db.create_all()
        db.session.commit()

    import_keywords()
