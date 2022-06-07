from config import db
from sqlalchemy import func, ForeignKey

class Compatible(db.Model):
    __tablename__ = 'compatible'
    id_motherboard = db.Column(db.Integer, ForeignKey('motherboard.id'), primary_key=True)
    id_component = db.Column(db.Integer, ForeignKey('component.id'), primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=func.now())
    create_by = db.Column(db.Integer, ForeignKey('userinfo.id'), nullable=False, default=0)

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
        return f'compatible: {self.id_motherboard}-{self.id_component}'