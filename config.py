import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')  or '4m3if035mwerd'
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    CSRF_ENABLED = True
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://USER:PASS@127.0.0.1/DBNAME'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
