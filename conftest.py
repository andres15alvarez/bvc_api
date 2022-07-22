import os
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE_HOST', 'database-2.c7p1u8khpvyi.us-west-2.rds.amazonaws.com'),
        'NAME': os.environ.get('DATABASE_NAME', 'plerk-develop'),
        'USER': os.environ.get('DATABASE_USER', 'plerk_develop'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'HQ1vfPA3bXWMmFm85Bqm'),
        'PORT': os.environ.get('DATABASE_PORT', 5432),
    }
