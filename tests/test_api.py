from nose.tools import *
from .common import Common
from models import User

class TestApi(Common):
	def teardown(self):
		u = User.query.filter_by(name=self.name).first()
		if u:
			u.delete()

	def test_user(self):
		#post
		self.name = 'test'
		r = self.post('/api/user', {'name': self.name, 'email': 'test@gmail.com', 'password': '123'})
		assert_in('test', str(r.data))

		u = User.query.filter_by(name=self.name).first()
		with self.app.session_transaction() as sess:
			sess['user_id'] = u.id

		#get
		assert_equal(200, self.get('/api/user/'+str(u.id)).status_code)

		#put
		r = self.put('/api/user', data={'name': self.name, 'email':
			'test1@gmail.com', 'password': '123'})
		assert_in('test1', str(r.data))

		#delete
		r = self.delete('/api/user/'+str(u.id))
		assert_in('"code": 0', str(r.data))
