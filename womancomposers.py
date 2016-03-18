import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen(" https://en.wikipedia.org/wiki/List_of_female_composers_by_birth_year").read()
soup = BeautifulSoup(page,"html.parser")
prettify=soup.prettify()
test=soup.find_all("a")
test=test[56:1318]

composers=[]
for element in test:
    composers.append(element.get_text())

for i in range(0, len(composers)-1):
    if len(composers[i])>1:
        composers[i]=composers[i].rsplit(" ")[-1]+", "+composers[i].rsplit(" ")[0]
    else: 
        composers[i]=composers[i]
print composers
