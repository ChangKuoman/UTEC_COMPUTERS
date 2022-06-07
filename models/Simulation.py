from config import db
from sqlalchemy import func, ForeignKey

class Simulation(db.Model):
    __tablename__ = 'simulation'
    id = db.Column(db.Integer, primary_key=True)
    id_motherboard = db.Column(db.Integer, ForeignKey('motherboard.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)
    total_price = db.Column(db.Float, nullable=False, default=0.0)

    simulation_components = db.relationship('SimulationComponent', backref='simulation', lazy=True, cascade="all, delete-orphan")

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

    def format(self):
        return {
            "id": self.id,
            "id_motherboard": self.id_motherboard,
            "total_price": self.total_price
        }

    def __repr__(self):
        return f'simulation: {self.id}'