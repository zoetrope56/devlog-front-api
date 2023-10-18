# import os
# from pathlib import Path
from configparser import ConfigParser

# basedir = os.path.dirname(os.path.abspath(__file__))
# basedir = Path(__file__).resolve().parent.parent.parent

conf = ConfigParser()
conf.read('.key_store.ini')

CONST_DB_HOST_DEBUG = conf['DB']['HOST_DEBUG']
CONST_DB_HOST_PROD = conf['DB']['HOST_PROD']
CONST_DB_PORT = int(conf['DB']['PORT'])
CONST_DB_USER = conf['DB']['USER']
CONST_DB_PW = conf['DB']['PW']
CONST_DB_NAME = conf['DB']['DB_NAME']
CONST_DB_CHARSET = conf['DB']['CHARSET']

SECRETKEY = conf['SECRET_KEY']