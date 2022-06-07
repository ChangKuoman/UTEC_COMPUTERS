from config import db
from sqlalchemy import func, ForeignKey

class Component(db.Model):
    __tablename__ = 'component'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(), nullable=False, unique=True)
    component_type = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)
    date_modified = db.Column(db.DateTime, nullable=False, default=func.now())
    modify_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)

    def __repr__(self):
        return f'component: {self.name}'
