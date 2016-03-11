import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.classical.net/music/composer/dates/comp7.php")
soup = BeautifulSoup(page)
prettify=soup.prettify()
nationality={}
h2=soup.find_all("h2")
li=soup.find_all("li")
lobbying = {}
for element in h2:
    lobbying[element.get_text()] = {}
    
for element in h2:
    name = element.find_all("li").get_text()
    lobbying[element.get_text()]["name"] = name
print lobbying