from sqlalchemy import Column, Integer, String
from .base import Base, CommonModel

class WebSite(Base, CommonModel):
	__tablename__ = 'website'
	title = Column(String(50), nullable=True)
	descr = Column(String(100))
	image = Column(String(100))
	url = Column(String(100), nullable=True)
	category_id = Column(Integer, nullable=True)
	visit_count = Column(Integer, default=0)
