import urllib2
import numpy
from bs4 import BeautifulSoup

#page = urllib2.urlopen("https://en.wikipedia.org/wiki/Category:Conductors_(music)_by_nationality").read()
page = urllib2.urlopen("https://en.wikipedia.org/wiki/Category:Classical_composers_by_nationality").read()
soup = BeautifulSoup(page,"html.parser")
prettify=soup.prettify()
nationality={}
test=soup.find_all("a", class_= "CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory")
test=test[1:-1]
#nationality={}
#prefix="https://en.wikipedia.org/"
#for element in test:
#    nationality[element.get_text()] = {}
#    nationality[element.get_text()["link"]]=prefix+element["href"]
  
nationality=[]
page=[]
nationalitypage=[]
prefix="https://en.wikipedia.org"
for element in test:
    nationality.append(element.get_text().split(" ")[0])
    page.append(prefix+element["href"]) 
nationalitypage=numpy.column_stack((nationality, page))
#page1=urllib2.urlopen("https://en.wikipedia.org/wiki/Category:Russian_conductors_(music)").read()
#soup1 = BeautifulSoup(page1,"html.parser")
#test1=soup1.find_all("li").find_all("a")

#<li><a href="/wiki/Valery_Afanassiev" title="Valery Afanassiev">Valery Afanassiev</a></li>
#<a class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:Uruguayan_conductors_(music)">Uruguayan conductors (music)</a>

print nationalitypage