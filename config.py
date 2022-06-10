import configparser
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

parser = configparser.ConfigParser()
parser.read("config.txt")

secret_key = parser.get("config", "secret_key")

username = parser.get("config", "username")
password = parser.get("config", "password")
host = parser.get("config", "host")
database_name = parser.get("config", "database_name")

database_path = f'postgresql://{username}:{password}@{host}/{database_name}'

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
    db.app = app
    db.init_app(app)
    db.create_all()
