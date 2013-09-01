from utills import *

class Code(RequestHandlerEx):
	def get(self):
		
		id = getIdFromUrl(self.request.url) # submission id
		if not isValidId(id):
			# TODO: go to 'not found'
			return
		data = DataStoreHelper.getEntryAsArray(id, True)
		if data == None:
			# TODO: go to 'not found'
			return
		code = data['code'] #source code
		
		self.o('<html>')
		self.o('<head>')
		self.o('	<style>%s</style>' % HtmlFormatter().get_style_defs('.highlight').replace('.highlight', ''))
		self.o('</head>')
		
		self.o('<body>')
		self.o(code)
		self.o('</body></html>')