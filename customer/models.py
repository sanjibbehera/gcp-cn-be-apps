from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP, func
from config.database import Base
    
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(String(50))
    last_name=Column(String(50))
    email=Column(String(50))
    user_name = Column(String(50))
    password=Column(String(100))
    created_date = Column(DateTime)
    modified_date = Column(TIMESTAMP, default=func.current_timestamp())
    isDeleted = Column(Integer, default=0)
    
