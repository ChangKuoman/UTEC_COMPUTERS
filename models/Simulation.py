from config import db
from sqlalchemy import func, ForeignKey

class Simulation(db.Model):
    __tablename__ = 'simulation'
    id = db.Column(db.Integer, primary_key=True)
    id_motherboard = db.Column(db.Integer, ForeignKey('motherboard.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)
    total_price = db.Column(db.Float, nullable=False, default=0.0)
    def __repr__(self):
        return f'simulation: {self.id}'