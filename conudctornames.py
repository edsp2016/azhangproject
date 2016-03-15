import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("https://en.wikipedia.org/wiki/Category:Conductors_(music)_by_nationality").read()
soup = BeautifulSoup(page,"html.parser")
prettify=soup.prettify()
nationality={}
a=soup.find_all("a", class_= "CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory")
a=a[1:-1]
nationality={}
for element in a:
    nationality[element.get_text()] = {}
    nationality[element.a.get_text()["link"]]=element.a["href"]
    
#test=soup.find("br/",{"class": "simpledot"})
print nationality