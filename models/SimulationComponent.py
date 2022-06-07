from config import db
from sqlalchemy import func, ForeignKey

class SimulationComponent(db.Model):
    __tablename__ = 'simulation_components'
    id_simulation = db.Column(db.Integer, ForeignKey('simulation.id'), primary_key=True)
    id_component = db.Column(db.Integer, ForeignKey('component.id'), primary_key=True)
    def __repr__(self):
        return f'simulation-compatible: {self.id_simulation}-{self.id_component}'
