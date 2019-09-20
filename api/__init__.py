from flask import Flask, jsonify
from config import Config
from database import db
from app import find_shortest_path
from config import StrListConverter



# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.converters['str_list'] = StrListConverter

# Initiate the database
db.init_app(app)


@app.before_first_request
def create_tables():
  db.create_all()


# App.route directs the output of the function directly below to the URL passed. "/" is the root address.
@app.route('/')
def index():
    return "Hello, World!"


@app.route('/mario/<int:n>/<str_list:grid>', methods=['GET'])
def get(n, grid):
  try:
    pp = find_shortest_path(n, grid)
  except Exception:
    return "Oops! That was not a valid grid. Try again"
  return jsonify(pp)

