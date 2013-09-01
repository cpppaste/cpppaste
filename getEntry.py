from utills import *

class GetEntry(RequestHandlerEx):
	def get(self):
		
		GET = cgi.FieldStorage()
		id = GET.getvalue('id');
		hlight = GET.getvalue('highlight');
		if not isValidId(id):
			self.o('invalid id [' + str(id) + ']')
			return;
		if not hlight:
			hlight = False;
		
		data = DataStoreHelper.getEntryAsArray(id, hlight)
		if data == None:
			self.o('0')
		else:
			self.o(json.dumps(data))