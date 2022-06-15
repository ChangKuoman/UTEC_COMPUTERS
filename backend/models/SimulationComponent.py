from config import db
from sqlalchemy import func, ForeignKey


class SimulationComponent(db.Model):
    __tablename__ = 'simulation_component'
    id_simulation = db.Column(db.Integer, ForeignKey('simulation.id'), primary_key=True)
    id_component = db.Column(db.Integer, ForeignKey('component.id'), primary_key=True)


    def format(self):
        return {
            "id_simulation": self.id_simulation,
            "id_component": self.id_component
        }


    def delete(self):
        try:
            self.simulation.delete()
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
        return f'simulation-compatible: {self.id_simulation}-{self.id_component}'
