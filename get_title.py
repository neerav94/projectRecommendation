import requests
from bs4 import BeautifulSoup


url = "http://cs229.stanford.edu/projects2014.html"
r = requests.get(url)
soup=BeautifulSoup(r.content)
#g_data1 = soup.find_all("a", {"class": "line"})
g_data1 = soup.find_all("b")
#print(g_data1)
for item in g_data1:
    #s = item["profile_name href"]
    print(item.text)
