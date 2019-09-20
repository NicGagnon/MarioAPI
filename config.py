# Config file for database
import os
from werkzeug.routing import BaseConverter

# Configuration variables to facilitate future refactoring or scaling
basedir = os.path.abspath(os.path.dirname(__file__))


# Configuration for SQLalchemy database
class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'api.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class StrListConverter(BaseConverter):
  regex = r'.+(?:,\.+)*,?'

  def to_python(self, value):
    return [str(x) for x in value.split(',')]

  def to_url(self, value):
    return ','.join(str(x) for x in value)
