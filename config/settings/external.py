from config.settings import *

DATABASES = {
    'default': {
        'NAME': CONST_DB_NAME,
        'ENGINE': 'django.db.backends.mysql',
        'USER': CONST_DB_USER,
        'PASSWORD': CONST_DB_PW,
        'HOST': CONST_DB_HOST_DEBUG,
        'PORT': CONST_DB_PORT,
        'OPTIONS': {
            'charset': CONST_DB_CHARSET,
        },
    }
}

SECRET_KEY = SECRETKEY

