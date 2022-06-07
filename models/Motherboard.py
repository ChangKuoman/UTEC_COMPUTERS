from config import db
from sqlalchemy import func, ForeignKey


class MotherBoard(db.Model):
    __tablename__ = 'motherboard'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)
    date_modified = db.Column(db.DateTime, nullable=False, default=func.now())
    modify_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)

    compatibles = db.relationship('Compatible', backref='motherboard', lazy=True, cascade="all, delete-orphan")
    simulations = db.relationship('Simulation', backref='motherboard', lazy=True, cascade="all, delete-orphan")


    def format(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
            "description": self.description
        }


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
        return f'motherboard: {self.name}'