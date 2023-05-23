import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # set postgres uri : DATABASE_URI="postgresql:/username:password@host:port/database_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    