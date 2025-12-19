from datetime import datetime
from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    
    user_id = Column('id', Integer, primary_key=True)
    username = Column(String(length=100), nullable=False, unique=True)
    password = Column(String(length=255), nullable=False)
    role = Column(String(length=20), nullable=False, default='user')
    
    token = relationship('AuthToken', back_populates='user')
    
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)