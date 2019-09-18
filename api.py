from flask import Flask
from flask_restful import Api
from config import Config
from database import db


# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)

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

# API endpoints
#api.add_resource(find_shortest_path, '/people')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
