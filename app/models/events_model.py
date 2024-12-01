from app.models import BaseModel
from sqlalchemy import Column,Integer,String,Boolean


class EventModel(BaseModel):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    photo = Column(String(255))
    fecha = Column(String(100))
    hora = Column(String(50))
    status = Column(Boolean, default=True)
    
