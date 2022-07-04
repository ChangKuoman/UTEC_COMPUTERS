from config import db
from sqlalchemy import func
import bcrypt
from uuid import uuid4
from datetime import timedelta

class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(), nullable=False, server_default='user')
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    date_modified = db.Column(db.DateTime, nullable=False, server_default=func.now())
    token = db.Column(db.String(36), unique=True, nullable=False)
    token_expire_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password, role='user'):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.password = hashed
        self.username = username
        self.role = role
        self.generate_token()


    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'token': self.token,
            'token_expire_date': self.token_expire_date
        }


    def check_password(self, password):
        if bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')):
            return True
        else:
            return False


    def generate_token(self):
        self.token = str(uuid4())
        self.token_expire_date = func.now() + timedelta(hours=1)


    def change_password(self, new_password):
        self.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.date_modified = func.now()


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
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def __repr__(self):
        return f'user: {self.username}'