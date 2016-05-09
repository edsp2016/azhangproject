from __future__ import unicode_literals
import urllib2
import numpy
from bs4 import BeautifulSoup
import pandas
#american (x)
#austrian 
#french (x)
#russian 
#itallian
#german
#czech
page = urllib2.urlopen("https://en.wikipedia.org/wiki/Category:French_classical_composers").read()
soup = BeautifulSoup(page,"html.parser")
test=soup.find_all("a", class_="external text")
page0=[]
everyone=[]
prefix="https:"
for element in test:
    page0.append(prefix+element["href"]) 
print page0
for i in range(0,len(page0)):
    names=[]
    page1=urllib2.urlopen(page0[i])
    soup1 = BeautifulSoup(page1,"html.parser")
    test1=soup1.find_all("a")
    for element in test1:
        names.append(element.get_text().encode('utf-8'))
    everyone.append(names) 
#print everyone
#my_df={}
#my_df=pandas.DataFrame(everyone)
#my_df.to_csv("germantest.csv",index=False,header=False,encoding='utf-8')


