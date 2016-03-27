# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib2
import numpy
from bs4 import BeautifulSoup
import pandas

page = urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_20th-century_classical_composers").read()
soup = BeautifulSoup(page,"html.parser")
test1=soup.find_all("td")
names=[]
years=[]
everyone=[]
for element in test1:
    test0=element.find_all("a")
    for element1 in test0:
         names.append(element1["title"].encode('utf-8'))
    years.append(element.get_text())
#my_df={}
#my_df=pandas.DataFrame(years)
#my_df.to_csv("twentiethC.csv",index=False,header=False,encoding='utf-8')
