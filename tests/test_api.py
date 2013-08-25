import json

from nose.tools import *
from .common import Common
from models import User

class TestApi(Common):
	def setup(self):
		self.name = 'test'

	def teardown(self):
		u = User.query.filter_by(name=self.name).first()
		if u:
			u.delete()
	
	def test_user(self):
		#post
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

		r = self.delete('/api/user/'+str(u.id))
		assert_in('"code": 1', str(r.data))

	def test_website(self):
		user_id = 1
		with self.app.session_transaction() as sess:
			sess['user_id'] = user_id

		#post
		r = self.post('/api/category', {'title': 'apple', 'descr': 'apple category'})
		data = self.jsonify_response_data()
		category_id = str(data.data.id)

		r = self.post('/api/website', {'title': 'ios', 'url':
			'http://www.apple.com.cn/ios/ios7/',
			'category_id': category_id,
			'descr': 'ios offical page'})
		assert_in('ios', str(r.data))
		data = self.jsonify_response_data()

		#get
		r = self.get('/api/website/'+str(data.data.id))
		assert_equal(data.data.id, self.jsonify_response_data().data.id)

		#put
		r = self.put('/api/website/'+str(data.data.id),
				{'title': 'ios', 'url':
			'http://www.apple.com.cn/ios/ios7/',
			'category_id': int(category_id),
			'descr': 'ios offical page abc'})
		assert_in('ios offical page abc', str(r.data))

		#delete
		r = self.delete('/api/website/'+str(data.data.id))
		assert_in('"code": 0', str(r.data))

		r = self.delete('/api/website/'+str(data.data.id))
		assert_in('"code": 1', str(r.data))

	def test_category(self):
		user_id = 1
		with self.app.session_transaction() as sess:
			sess['user_id'] = user_id

		#post
		r = self.post('/api/category', {'title': 'apple', 'descr': 'apple category'})
		assert_in('apple', str(r.data))
		data = json.loads(r.data.decode('utf8'))
		category_id = str(data['data']['id'])

		#get
		r = self.get('/api/category/'+category_id)
		assert_equal(200, r.status_code)

		#put
		r = self.put('/api/category/'+category_id, {'title': 'apple1', 'descr': 'apple category'})
		assert_in('apple1', str(r.data))
		data = json.loads(r.data.decode('utf8'))
		assert_equal(int(category_id), data['data']['id'])

		#delete
		r = self.delete('/api/category/'+category_id)
		assert_in('"code": 0', str(r.data))

		r = self.delete('/api/category/'+category_id)
		assert_in('"code": 1', str(r.data))
