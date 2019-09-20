from flask import Flask, jsonify
from config import Config
from database import db
from app import find_shortest_path
from config import StrListConverter
from models.mario import MarioModel


# Create an instance of flask, configs, and strlist converter
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
def mario(n, grid):
    # Find shortest paths, create mario instance from paths and save to database
    try:
      pp = find_shortest_path(n, grid)
      new_mario = MarioModel(n, grid, pp)
      new_mario.save_to_db()
      return jsonify(pp)
    except Exception as e:
      print(e)
      return "Oops! That was not a valid grid. Try again"


# endpoint to get log detail by id
@app.route("/log", methods=["GET"])
def log_detail():
    # Return all logs from the database
    all_mario = MarioModel.query.all()
    j_marios = [mario.json() for mario in all_mario]
    return jsonify(j_marios)
