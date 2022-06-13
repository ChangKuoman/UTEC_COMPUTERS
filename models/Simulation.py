from config import db
from sqlalchemy import func, ForeignKey
from models.Component import Component
from models.MotherBoard import MotherBoard

class Simulation(db.Model):
    __tablename__ = 'simulation'
    id = db.Column(db.Integer, primary_key=True)
    id_motherboard = db.Column(db.Integer, ForeignKey('motherboard.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)
    total_price = db.Column(db.Float, nullable=False, server_default='0.0')

    simulation_components = db.relationship('SimulationComponent', backref='simulation', lazy=True, cascade="all, delete-orphan")


    def format(self):
        return {
            "create_by": self.create_by,
            "id": self.id,
            "motherboard": MotherBoard.query.get(self.id_motherboard).format(),
            "total_price": self.total_price,
            "components": {component.id_component:Component.query.get(component.id_component).format() for component in self.simulation_components}
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
        return f'simulation: {self.id}'