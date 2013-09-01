import re

class Validator:
	
	@staticmethod
	def validateUserName(username):
		if '\n' in username:
			return False
		return re.match('^\w{3,50}$', username) != None
		
	@staticmethod
	def validateUserPassword(password):
		if '\n' in password:
			return False
		return re.match('^\w{6,50}$', password) != None