import cgi
import random
import os
import sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

submission_length = 8

def getIdLength():
	return submission_length
	
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
	
class Entry(db.Model):
	code =    db.TextProperty()
	comment = db.StringProperty(multiline = False)
	date =    db.DateTimeProperty(auto_now_add = True)
	lang =    db.StringProperty(multiline = False)
	id =      db.StringProperty(multiline = False)
	IP =      db.StringProperty(multiline = False)
	
