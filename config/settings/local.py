# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .common import *  # noqa

THUMBNAIL_DEBUG = True

CACHES = {
    'default': env.cache("CACHE_LOCATION", default="filecache://tmp/django_cache")
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

DEBUG=env.bool('DEBUG', default=True)
