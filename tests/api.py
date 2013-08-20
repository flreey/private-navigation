from .common import Common

class Api(Common):
	def test_user(self):
		print(self.app.get('/api/user/1'))
