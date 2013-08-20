import hashlib

from sqlalchemy import Column, Integer, String
from .base import Base, CommonModel

class User(Base, CommonModel):
	__tablename__ = 'user'
	name = Column(String(50), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)
	password = Column(String(60), nullable=False)

	def insert(self):
		self.password = self._encrypt_password(self.password)
		return super().insert()

	def valid_password(self, password):
		return self.password == self._encrypt_password(password)

	def _encrypt_password(self, password):
		from flask import current_app

		salt = current_app.config['PASSWORD_SALT']
		password = (salt + password).encode('utf8')
		return hashlib.md5(password).hexdigest()
