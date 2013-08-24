import cgi, imp, sys

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

sys.path.append("Admin")

from utills import *
from DataStoreHelper import *

from code import *
from getEntry import *
from admin_login import *


class Main(webapp.RequestHandler):

	languages = ['C++', 
				 'Java',
				 'Python',
				 'Other...'
				]
	
	def getLanguageFormPart(self):
		self.response.out.write('<select id=language name=lang class=shadow>');
		for language in self.languages:
			self.response.out.write('<option>' + language + '</option>');
		self.response.out.write('</select>');

	def get(self):

		self.response.out.write('<html>')
		self.response.out.write('<head>')
		self.response.out.write('<link rel="stylesheet" type="text/css" href="css/style.css" />')
		self.response.out.write('<script src="js/jQuery.js"></script>')
		self.response.out.write('<script src="js/main.js"></script>')
		self.response.out.write('</head>')
		self.response.out.write('<body>')

		self.response.out.write('<form action="submit" method="post">')
		self.response.out.write('<table class="tableStyle">')
		self.response.out.write('<tr class="langRow">')
		self.response.out.write('<td>')
		self.getLanguageFormPart()
		self.response.out.write('</td>')
		self.response.out.write('</tr>')
 
		self.response.out.write('''<tr class="commentRow"> 
			<td><div class=textStyle>Comment:</div></td>
			<td><input class="textareaStyle shadow" type="text" name="comment"><br></td>
		</tr>
 
		<tr>
			<td colspan="2"><textarea name="code" class="textareaStyle shadow"></textarea></td>
		</tr>
  
		<tr class="submitRow">
			<td><input id=submit onclick="submitAction()" class="button" type="submit" value="Submit"></td>
		</tr>
 
		</table> 
 </form>
</body>
</html>''')




application = webapp.WSGIApplication(
                                     [
										('/', Main),
										('/code/.*', Code),
										('/getentry', GetEntry),
										('/admin-login', AdminLogin)
									 ],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()



