from sqlalchemy import Column, Integer, String
from .base import Base, CommonModel

class WebSite(Base, CommonModel):
	__tablename__ = 'website'
	title = Column(String(50), nullable=False)
	descr = Column(String(100))
	image = Column(String(100))
	url = Column(String(100), nullable=False)
	visit_count = Column(Integer, default=0)
	category_id = Column(Integer, nullable=False)
