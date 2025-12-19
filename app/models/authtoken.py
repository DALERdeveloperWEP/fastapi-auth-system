from app.db.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class AuthToken(Base):
    __tablename__ = 'token'
    
    token_id = Column('id', Integer, primary_key=True)
    token = Column(String(length=128), nullable=False, unique=True)
    expires_date = Column(DateTime)
    user_id=Column(ForeignKey('users.id', onupdate='CASCADE'))
    
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('Users', back_populates='token')
    