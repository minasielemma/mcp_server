from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    user_id = Column(String, nullable=True)

class EmailAnalysis(Base):
    __tablename__ = "email_analysis"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    email_id = Column(String,index=True)
    sender = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    analysis = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
