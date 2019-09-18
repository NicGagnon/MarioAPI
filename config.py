# Config file for database
#
import os

# Configuration variables to facilitate future refactoring or scaling
basedir = os.path.abspath(os.path.dirname(__file__))


# Configuration for SQLalchemy database
class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'api.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
