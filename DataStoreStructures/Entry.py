from google.appengine.ext import db

class Entry(db.Model):
	code =    db.TextProperty()
	comment = db.StringProperty(multiline = False)
	date =    db.DateTimeProperty(auto_now_add = True)
	lang =    db.StringProperty(multiline = False)
	id =      db.StringProperty(multiline = False)
	IP =      db.StringProperty(multiline = False)