from nose.tools import *
from .common import Common
from models import User

class TestApi(Common):
	def teardown(self):
		u = User.query.filter_by(name=self.name).first()
		if u:
			u.delete()

	def test_user(self):
		assert_equal(200, self.get('/api/user/1').status_code)
		self.name = 'test'
		r = self.post('/api/user', {'name': self.name, 'email': 'test@gmail.com', 'password': '123'})
		assert_in('test', str(r.data))
