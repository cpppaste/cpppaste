from utills import *

sys.path.append("Auth")

from code import *
from getEntry import *
from auth import *

class Main(RequestHandlerEx):

	languages = ['C++', 
				 'Java',
				 'Python',
				 'Other...'
				]
	
	def getLanguageFormPart(self):
		self.o('<select id=language name=lang class=shadow>');
		for language in self.languages:
			self.o('<option>' + language + '</option>');
		self.o('</select>');

	def get(self):

		self.o('<html>')
		self.o('<head>')
		self.o('<link rel="stylesheet" type="text/css" href="css/style.css" />')
		self.o('<script src="js/jQuery.js"></script>')
		self.o('<script src="js/main.js"></script>')
		self.response.out.write('</head>')
		self.response.out.write('<body>')

		self.o('<form action="submit" method="post">')
		self.o('<table class="tableStyle">')
		self.o('<tr class="langRow">')
		self.o('<td>')
		self.getLanguageFormPart()
		self.o('</td>')
		self.o('</tr>')
 
		self.o('''<tr class="commentRow"> 
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
										('/auth', Auth)
									 ],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()



