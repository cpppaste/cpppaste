import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from utills import *
from getEntry import *

sys.path.append("Pygments")
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def getIdFromUrl(url):
	url = url[-getIdLength()::]
	if url.isalpha():
		return url
	return "none"

class Code(webapp.RequestHandler):
	def get(self):
		
		self.response.out.write('<html>')
		self.response.out.write('<head>')
		self.response.out.write('<style>%s</style>' % HtmlFormatter().get_style_defs('.highlight').replace('.highlight', ''))
		self.response.out.write('<script src="%s"></script>' % 'http://localhost:8080/js/getEntry.js')
		self.response.out.write('<script src="%s"></script>' % 'http://localhost:8080/js/jQuery.js')
		self.response.out.write('</head>')
		
		self.response.out.write('<body>')
		self.response.out.write('<script>getEntry("zuhlqoct", false);</script>')
		
		id = getIdFromUrl(self.request.url)
		
		entries = db.GqlQuery("SELECT * FROM Entry WHERE id='%s'" % id)
		for entry in entries:
			lexer = get_lexer_by_name(LanguagePygments[entry.lang], stripall = True)
			formatter = HtmlFormatter(linenos  = False, cssclass = "source")
			htmlcode = highlight(entry.code, lexer, formatter)
			self.response.out.write(htmlcode)
		
		
		self.response.out.write('</body></html>')

application = webapp.WSGIApplication(
                                     [
										('/code/.*', Code),
										('/getentry', GetEntry)
									 ],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()