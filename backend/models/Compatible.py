from config import db
from sqlalchemy import func, ForeignKey
from models.Component import Component
from models.MotherBoard import MotherBoard


class Compatible(db.Model):
    __tablename__ = 'compatible'
    compatible_id_seq = db.Sequence('cart_id_seq')
    id = db.Column(db.Integer, compatible_id_seq, server_default=compatible_id_seq.next_value(), nullable=False, unique=True)
    id_motherboard = db.Column(db.Integer, ForeignKey('motherboard.id'), primary_key=True)
    id_component = db.Column(db.Integer, ForeignKey('component.id'), primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False)


    def format(self):
        return {
            "id": self.id,
            "id_motherboard": self.id_motherboard,
            "id_component": self.id_component,
            "motherboard": MotherBoard.query.get(self.id_motherboard).name,
            "component": Component.query.get(self.id_component).name
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
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()


    def __repr__(self):
        return f'compatible: {self.id_motherboard}-{self.id_component}'