import cgi
import random
import os
import sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from utills import *



class Submit(webapp.RequestHandler):
	def post(self):
		entry = Entry()
		entry.code = self.request.get('code')
		entry.lang = self.request.get('lang')
		entry.comment = self.request.get('comment')
		entry.id = getRandString(submission_length)
		entry.IP = self.request.remote_addr
		entry.put()
		self.redirect( '/code/%s' % entry.id )

application = webapp.WSGIApplication(
                                     [('/submit', Submit)],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()


