from config import db
from sqlalchemy import func, ForeignKey

class Component(db.Model):
    __tablename__ = 'component'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(), nullable=False, unique=True)
    component_type = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False, server_default=func.now())
    modify_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False)

    compatibles = db.relationship('Compatible', backref='component', lazy=True, cascade="all, delete-orphan")
    simulation_components = db.relationship('SimulationComponent', backref='component', lazy=True, cascade="all, delete-orphan")


    def __init__(self, description, name, component_type, price, create_by):
        self.description=description,
        self.name=name,
        self.component_type=component_type,
        self.price=price,
        self.create_by=create_by
        self.modify_by=create_by


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'component_type': self.component_type,
            'description': self.description,
            'price': self.price
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
            self.date_modified = func.now()
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def __repr__(self):
        return f'component: {self.name}'
