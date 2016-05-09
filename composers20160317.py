from __future__ import unicode_literals
import urllib2
import numpy
from bs4 import BeautifulSoup
import pandas
page = urllib2.urlopen("https://en.wikipedia.org/wiki/Category:Classical_composers_by_nationality").read()
soup = BeautifulSoup(page,"html.parser")
prettify=soup.prettify()
nationality={}
test=soup.find_all("a", class_= "CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory")
test=test[1:-1]
nationality=[]
namesForOneCountry=[[]]
namesForEveryone=[]
page=[]
nationalitypage=[]
prefix="https://en.wikipedia.org"
for element in test:
    nationality.append(element.get_text().split(" ")[0])
    page.append(prefix+element["href"]) 
nationalitypage=numpy.column_stack((nationality, page))
for i in range(0,len(nationalitypage)):
    namesForOneCountry=[]
    page1=urllib2.urlopen(nationalitypage[i][1])
    soup1 = BeautifulSoup(page1,"html.parser")
    #print soup1
    test1=soup1.find_all("a")
    for element in test1:
        namesForOneCountry.append(element.get_text().encode('utf-8'))
    namesForEveryone.append(namesForOneCountry)
my_df={}
for i in range(0, len(namesForEveryone)-1):
    my_df[i]=pandas.DataFrame(namesForEveryone[i])
    str1=nationalitypage[i][0]
    str2=".csv"
    str3=str1+str2
    my_df[i].to_csv(str3,index=False,header=False,encoding='utf-8')


#https://en.wikipedia.org/wiki/List_of_Austrian_composers
#american
#austrian 
#french