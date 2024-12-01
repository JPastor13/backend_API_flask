from app.models import BaseModel
from sqlalchemy import Column, Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship

class PromotionModel(BaseModel):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.id'))
    title = Column(String(150))
    photo = Column(String(255))
    status = Column(Boolean, default=True)

    store = relationship('StoreModel', uselist=False)


