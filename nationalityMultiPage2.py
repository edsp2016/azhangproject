from __future__ import unicode_literals
import urllib2
import numpy
from bs4 import BeautifulSoup
import pandas
#austrian 

page = urllib2.urlopen("https://en.wikipedia.org/w/index.php?title=Category:French_classical_composers&pagefrom=Ollone%2C+Max+d%0AMax+d%27Ollone#mw-pages").read()
soup = BeautifulSoup(page,"html.parser")
test=soup.find_all("a")
names=[]
for element in test:
    names.append(element.get_text().encode('utf-8'))
print names
my_df={}
my_df=pandas.DataFrame(names)
my_df.to_csv("frenchtest4.csv",index=False,header=False,encoding='utf-8')