class Config:
	DEBUG = False
	TESTING = False
	SECRET_KEY = b'X\xa5-\xb8>\xd0\x04\xa8Z\xee\x88L\xb2\x89\xab\xde\xcb\xe6\x9c\xbd'

class DevelpmentConfig(Config):
	DEBUG = True
	TESTING = True
	DATABASE_URI = 'sqlite:////tmp/test.db'

class ProductionConfig(Config):
	DATABASE_URI = ''
