from sqlalchemy import Column, Integer, String, Boolean
from .base import Base, CommonModel

class Category(Base, CommonModel):
	__tablename__ = 'category'
	parent = Column(Integer, default=0)
	title = Column(String(50), nullable=False)
	descr = Column(String(100))
	is_valid = Column(Boolean(), default=True)
	user_id = Column(Integer, nullable=False)
	order = Column(Integer, default=0)
