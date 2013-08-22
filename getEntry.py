from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from utills import *
from DataStoreHelper import *
import json
import cgi

class GetEntry(webapp.RequestHandler):
	def get(self):
		
		GET = cgi.FieldStorage()
		id = GET.getvalue('id');
		hlight = GET.getvalue('highlight');
		if not isValidId(id):
			self.response.out.write('invalid id [' + str(id) + ']')
			return;
		if not hlight:
			hlight = False;
		
		data = DataStoreHelper.getEntryAsArray(id, hlight)
		if data == None:
			self.response.out.write('0')
		else:
			self.response.out.write(json.dumps(data))