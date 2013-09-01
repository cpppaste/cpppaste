from google.appengine.ext import db

class User(db.Model):
	username = db.StringProperty(multiline = False)
	password = db.StringProperty(multiline = False)
	admin    = db.StringProperty(multiline = False)