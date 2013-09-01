import cgi
import random
import os
import sys
import json

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

sys.path.append("Utills")
from validator import Validator
from hashing import Hasher

class RequestHandlerEx(webapp.RequestHandler):
	def o(self, object):
		self.response.out.write(object)


submission_length = 8

def getIdLength():
	return submission_length

def getIdFromUrl(url):
	url = url[-getIdLength()::]
	if url.isalpha():
		return url
	return "none"

def isValidId(id):
	if not id:
		return False
	if len(id) != getIdLength():
		return False
	if not id.isalpha():
		return False
	return True

LanguagePygments = {
	"C++" :      "cpp",
	"Java" :     "java",
	"Other..." : "text",
	"Python" :   "python"
}

def getRandString(length):
	result = ""
	for i in range(length):
		result += chr(random.randint(ord('a'), ord('z')))
	return result

MAX_LEN = 1000000





sys.path.append("Pygments")
sys.path.append("DataStoreStructures")
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from Entry import Entry
from User import User

class DataStoreHelper:

	@staticmethod
	def getEntryAsArray(id, hlight):
		result = DataStoreHelper.getEntriesAsArrays("id='%s'" % id)
		if hlight:
			result = DataStoreHelper.highLight(result)
		if len(result) != 1:
			return None
		return result[0]

	@staticmethod
	def getEntriesAsArrays(db_where = ''):
		entries = db.GqlQuery("SELECT * FROM Entry" + (" WHERE " if db_where else "") + db_where)
		result = []
		for entry in entries:
			result.append({
				'code':     str(entry.code),
				'comment' : str(entry.comment),
				'date' :    str(entry.date),
				'lang' :    str(entry.lang),
				'id' :      str(entry.id)
			})
		return result

	@staticmethod
	def highLight(data):
		if type(data) == list:
			return [DataStoreHelper.highLight(item) for item in data]

		lexer = get_lexer_by_name(LanguagePygments[data['lang']], stripall = True)
		formatter = HtmlFormatter(linenos  = False, cssclass = "source")
		code = highlight(data['code'], lexer, formatter)

		return {
			'code':     code,
			'comment' : data['comment'],
			'date' :    data['date'],
			'lang' :    data['lang'],
			'id' :      data['id']
		}