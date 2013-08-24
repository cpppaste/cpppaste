#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db



from utills import *
from DataStoreHelper import *

from code import *
from getEntry import *
from validator import Validator

class AdminLogin(webapp.RequestHandler):

	def o(self, object):
		self.response.out.write(object)
	
	def outputAdminEnterForm(self):
		#self.o(' <form action="admin-login" method="post">')
		#self.o(' 	<div class="admin-login-form-wrapper">')
		#self.o(' 		<input class="admin-login-text" type="text" name="username">')
		#self.o(' 		<input class="admin-login-text" type="password" name="password">')
		#self.o(' 	</div>')
		#self.o(' 	<input class="admin-login-button" type="submit" value="Login">')
		#self.o(' </form>')
		
		self.o('''
		
		<html>
		<head>
			<link rel="stylesheet" type="text/css" href="''' + 'css/login.css' + '''" />
			<style>
				body {
					background: #7f9b4e url(images/bg2.jpg) no-repeat center top;
					-webkit-background-size: cover;
					-moz-background-size: cover;
					background-size: cover;
				}
			</style>
		</head>
		<body>

				<form action="admin-login" class="form-4" method="post">
				    <h1>Auth</h1>
				    <p>
				        <label for="username">Username</label>
				        <input type="text" name="username" placeholder="Username" required>
				    </p>
				    <p>
				        <label for="password">Password</label>
				        <input type="password" name='password' placeholder="Password" required> 
				    </p>

				    <p>
				        <input type="submit" name="submit" value="Log in">
				    </p>       
				</form>


	</body>
	</html>

''')
		
	
	def get(self):
		self.outputAdminEnterForm()
		
	def post(self):
	
		POST = cgi.FieldStorage()
		username = POST.getvalue('username');
		password = POST.getvalue('password');
		
		# registration
		#if username == 'admin':
		#	user = User()
		#	user.username = 'admin'
		#	user.password = ''
		#	user.put()
		#	self.o('registered')
		#	return
		
		if not Validator.validateUserName(username) or not Validator.validateUserPassword(password):
			self.o('invalid data')
			return
			
		users = db.GqlQuery("SELECT * FROM User WHERE username='%s' AND password='%s'" % (username, password))
		
		if users.count() == 0:
			self.o('wrond username or password')
			return
		
		self.o('OK')
		
	