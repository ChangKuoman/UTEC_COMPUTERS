from config import db
from flask_login import UserMixin
from sqlalchemy import func
import bcrypt
from uuid import uuid4

class User(db.Model, UserMixin):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(), nullable=False, server_default='user')
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())


    def __init__(self, username, password, role='user'):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.password = hashed
        self.username = username
        self.role = role

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }


    def check_password(self, password):
        if bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')):
            return True
        else:
            return False


    def generate_key(self):
        return uuid4()


    def change_password(self, new_password):
        self.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def __repr__(self):
        return f'user: {self.username}'