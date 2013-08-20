import app as pn

class Common:
	def __init__(self):
		pn.app.config['TESTING'] = True
		self.app = pn.app.test_client()

	def setup(self):
		pass

	def teardown(self):
		pass

	def get(self, uri):
		r = self.app.get(uri)
		print(r.data)
		return r

	def post(self, uri, data=None):
		r = self.app.post(uri, data=data)
		print(r.data)
		return r
