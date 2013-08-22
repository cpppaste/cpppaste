import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from utills import *
from DataStoreHelper import *

class Code(webapp.RequestHandler):
	def get(self):
		
		id = getIdFromUrl(self.request.url) # submission id
		if not isValidId(id):
			# TODO: go to 'not found'
			return
		data = DataStoreHelper.getEntryAsArray(id, True)
		if data == None:
			# TODO: go to 'not found'
			return
		code = data['code'] #source code
		
		self.response.out.write('<html>')
		self.response.out.write('<head>')
		self.response.out.write('<style>%s</style>' % HtmlFormatter().get_style_defs('.highlight').replace('.highlight', ''))
		self.response.out.write('</head>')
		
		self.response.out.write('<body>')
		
		self.response.out.write(code)
		
		self.response.out.write('</body></html>')