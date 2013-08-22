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

class DataStoreHelper:
	
	@staticmethod
	def getEntryAsArray(id, hlight):
		entries = db.GqlQuery("SELECT * FROM Entry WHERE id='%s'" % id)
		for entry in entries:
			code = entry.code
			if hlight:
				lexer = get_lexer_by_name(LanguagePygments[entry.lang], stripall = True)
				formatter = HtmlFormatter(linenos  = False, cssclass = "source")
				code = highlight(code, lexer, formatter)
				
			return {
				'code':     str(code),
				'comment' : str(entry.comment),
				'date' :    str(entry.date),
				'lang' :    str(entry.lang),
				'id' :      str(entry.id)
			}
			return;
		return None