from app.models import BaseModel
from sqlalchemy import Column, Integer, String,Boolean

class StoreModel(BaseModel):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True)
    stand = Column(String(3), nullable=False)
    name = Column(String(100), nullable=False)
    logo = Column(String(255))
    phone = Column(String(20))
    days_open = Column(String(50))
    schedule =  Column(String(50))
    level = Column(String(100))
    title =  Column(String(150))
    description =  Column(String(255))
    photo_menu_1 = Column(String(255))
    photo_menu_2 = Column(String(255))
    photo_menu_3 = Column(String(255))
    photo_primary = Column(String(255))
    status = Column(Boolean, default=True)



'''
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    es_administrador = db.Column(db.Boolean, default=False)

    asignaciones = db.relationship('AsignacionTienda', backref='usuario', cascade="all, delete")
'''
