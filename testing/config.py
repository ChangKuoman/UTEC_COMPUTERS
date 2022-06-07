import configparser
from flask_sqlalchemy import SQLAlchemy
import configparser

db = SQLAlchemy()

parser = configparser.ConfigParser()
parser.read("config.txt")

username = parser.get("config", "username")
password = parser.get("config", "password")
host = parser.get("config", "host")
database_name = parser.get("config", "database_name")

database_path = f'postgresql://{username}:{password}@{host}/{database_name}'

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()
