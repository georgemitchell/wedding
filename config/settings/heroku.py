from .common import *  # noqa

DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres:///postgres"),
}
