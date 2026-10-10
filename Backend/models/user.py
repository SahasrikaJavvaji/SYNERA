
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    company_name = Column(String(150), nullable=False)
    location = Column(String(150), nullable=False)
    contact = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

