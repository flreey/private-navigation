import json

from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import current_app

engine = create_engine(current_app.config['DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
	autoflush=False,
	bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	# import all modules here that might define models so that
	# they will be registered properly on the metadata.  Otherwise
	# you will have to import them first before calling init_db()
	from .user import User
	from .category import Category
	from .website import WebSite
	Base.metadata.create_all(bind=engine)

class CommonModel:
	id = Column(Integer, primary_key=True)
	create_at = Column(DateTime(), default=datetime.now)
	update_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

	@classmethod
	def get(cls, id):
		return cls.query.filter_by(id=id).first()

	def insert(self, autocommit=True):
		db_session.add(self)
		if autocommit:
			db_session.commit()
		return self

	update = insert

	def delete(self, autocommit=True):
		db_session.delete(self)
		if autocommit:
			db_session.commit()
		return self

	@property
	def json(self):
		result = {}
		for k, v in self.__dict__.items():
			if issubclass(type(v), datetime):
				v = datetime.strftime(v, '%Y-%m-%d %H:%M:%S')
			if not k.startswith('_') and k != 'password':
				result[k] = v
		return result

	def __repr__(self):
		return json.dumps(self.json, indent=2)
