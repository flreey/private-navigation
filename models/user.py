from sqlalchemy import Column, Integer, String
from .base import Base, CommonModel

class User(Base, CommonModel):
	__tablename__ = 'user'
	name = Column(String(50), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)
	password = Column(String(60), nullable=False)
