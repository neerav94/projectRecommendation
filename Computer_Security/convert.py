import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO

#def pdfparser(data):
for i in range(41, 95):
	j=str(i)+".txt"
	f = open(j,"w")
	k=str(i)+".pdf"
	fp = file(k, 'rb')
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	# Create a PDF interpreter object.
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	# Process each page contained in the document.

	for page in PDFPage.get_pages(fp):
    		interpreter.process_page(page)
    		data =  retstr.getvalue()
    		f.write(data)
	#print data
	f.close()
print "done"

#pdfparser(sys.argv[1]) 
