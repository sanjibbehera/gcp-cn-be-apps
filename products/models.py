from sqlalchemy import ARRAY, TIMESTAMP, Column, ForeignKey, Integer, String, DateTime, text, Numeric
from config.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)    
    image_url = Column(String(255), nullable=False)
    manufacturer = Column(String(255), nullable=False)