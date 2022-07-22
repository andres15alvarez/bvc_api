import os
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'PORT': os.environ.get('DATABASE_PORT', 5432),
    }
