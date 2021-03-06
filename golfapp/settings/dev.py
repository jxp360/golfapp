#!/usr/bin/env python

from golfapp.settings.common import *

DB_BASE_DIR = '/data/workspace/golfapp/dbs/dev'

INSTALLED_APPS = (
    'bootstrap3',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'golfapp.apps.golfstats',
    'golfapp.apps.piffycup',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#AUTHENTICATION_BACKENDS = (
#    'mongoengine.django.auth.MongoEngineBackend',
#)

INTERNAL_IPS = (
    '127.0.0.1',
)

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.dummy',
#    }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_BASE_DIR, 'golfapp.db'),
    }
}

#connect('golfapp')
