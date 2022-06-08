from config import db
from flask_login import UserMixin
from sqlalchemy import func
import bcrypt

class User(db.Model, UserMixin):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(), nullable=False, server_default='user')
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())


    def __init__(self, username, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.password = hashed
        self.username = username


    def check_password(self, password):
        if bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')):
            return True
        else:
            return False


    def __repr__(self):
        return f'user: {self.username}'