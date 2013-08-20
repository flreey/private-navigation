from nose.tools import *
from .common import Common

class TestApi(Common):
	def test_user(self):
		assert_equal(200, self.get('/api/user/1').status_code)
		print(self.post('/api/user', {'name': 'test', 'email': 'test@gmail.com', 'password': '123'}))
