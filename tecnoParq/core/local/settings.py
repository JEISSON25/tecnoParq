from ..settings import *  # noqa: F403, F401


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbvotoe',
        'USER': 'ingejeisson',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True
