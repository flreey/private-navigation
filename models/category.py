from sqlalchemy import Column, Integer, String, Boolean
from .base import Base, CommonModel

class Category(Base, CommonModel):
	__tablename__ = 'category'
	parent = Column(Integer, default=0)
	user_id = Column(Integer, nullable=True)
	title = Column(String(50), nullable=True)
	descr = Column(String(100))
	is_valid = Column(Boolean(), default=True)
