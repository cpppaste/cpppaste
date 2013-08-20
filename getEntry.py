import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from utills import *
import json
import cgi

sys.path.append("Pygments")
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

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
		
		entries = db.GqlQuery("SELECT * FROM Entry WHERE id='%s'" % id)
		for entry in entries:
			code = entry.code
			if hlight:
				lexer = get_lexer_by_name(LanguagePygments[entry.lang], stripall = True)
				formatter = HtmlFormatter(linenos  = False, cssclass = "source")
				code = highlight(code, lexer, formatter)
				
			self.response.out.write(json.dumps({
				'code':     str(code),
				'comment' : str(entry.comment),
				'date' :    str(entry.date),
				'lang' :    str(entry.lang),
				'id' :      str(entry.id)
			}))
			return;
		self.response.out.write('0')
			