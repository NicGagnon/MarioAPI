from flask import Flask, jsonify
from flask_restful import Api, Resource, request
from config import Config
from database import db
from app import find_shortest_path
from werkzeug.routing import BaseConverter
import json

class StrListConverter(BaseConverter):
  regex = r'.+(?:,\.+)*,?'

  def to_python(self, value):
    return [str(x) for x in value.split(',')]

  def to_url(self, value):
    return ','.join(str(x) for x in value)

# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.converters['str_list'] = StrListConverter

# Initiate the database
db.init_app(app)

# Create an instance of flask Restful
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()


# App.route directs the output of the function directly below to the URL passed. "/" is the root address.
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/mario/<int:n>/<str_list:grid>', methods=['GET'])
def mario(n, grid):
  try:
    #n = request.args.get('n', None)
    #grid = request.args.get('grid', None)
    pp = find_shortest_path(n, grid)
  except Exception:
    return "Oops! That was not a valid grid.   Try again"
  return jsonify(pp)


# API endpoints
# api.add_resource(find_shortest_path, '/mario/{}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
