from utills import *

class Auth(RequestHandlerEx):
	
	def outputAdminEnterForm(self):
		
		self.o('''
			<form action="auth" class="form-4" method="post">
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
		''')
		
	
	def get(self):
		self.o('''
			<html>
			<head>
				<title>Auth</title>
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
		''')
		self.outputAdminEnterForm()
		self.o('''
			</body>
			</html>
		''')
		
	def post(self):
	
		POST = cgi.FieldStorage()
		username = POST.getvalue('username');
		password = POST.getvalue('password');
		
		# registration
		#if username == 'admin':
		#	user = User()
		#	user.username = 'admin'
		#	user.password = str(Hasher.getPolinomialHash(password))
		#	user.admin = '1'
		#	user.put()
		#	self.o('registered')
		#	return
		
		if not Validator.validateUserName(username) or not Validator.validateUserPassword(password):
			self.o('invalid data')
			return
		
		password = str(Hasher.getPolinomialHash(password))
		users = db.GqlQuery("SELECT * FROM User WHERE username='%s' AND password='%s'" % (username, password))
		
		if users.count() == 0:
			self.o('wrond username or password')
			return
		
		self.o('OK')
		
	