import requests 
from bs4 import BeautifulSoup
count=0
url = "http://web.stanford.edu/class/ee368/Project_Spring_1314/index.html"
r = requests.get(url)
soup=BeautifulSoup(r.content)
for a in soup.find_all('a', href=True):
	count+=1
	link = a['href']
	print link

print "done"

#"https://stacks.stanford.edu/file/druid:bf950qp8995/Choksi.pdf"
#<a href="https://stacks.stanford.edu/file/druid:bf950qp8995/Liu_Xiao.pdf"
