import xml.etree.ElementTree as ET
import urllib2
import numpy
#import csv
data=urllib2.urlopen("https://raw.githubusercontent.com/nyphilarchive/PerformanceHistory/master/Programs/1842-43_TO_1910-11.xml")
root=ET.parse(data).getroot()
id=[]
programid=[]
orchestra=[]
season=[]
eventType=[]
Location=[]
Venue=[]
Date=[]
Time=[]
program=[]
concertInfo=[]
workID0=[]
composerName0=[]
workTitle0=[]
conductorName0=[]
interval=[]
movement=[]
soloistName=[]
soloistInstrument=[]
soloistRoles=[]
for i in range(0,len(root)-1):
    id.append(root.findall("program")[i].find("id").text)
    programid.append(root.findall("program")[i].find("programID").text)
    orchestra.append(root.findall("program")[i].find("orchestra").text)
    season.append(root.findall("program")[i].find("season").text)
    program=numpy.column_stack((id,programid,orchestra, season))
    eventType.append(root.findall("program")[i].findall("concertInfo")[0].find("eventType").text)
    Location.append(root.findall("program")[i].findall("concertInfo")[0].find("Location").text)
    Venue.append(root.findall("program")[i].findall("concertInfo")[0].find("Venue").text)
    Date.append(root.findall("program")[i].findall("concertInfo")[0].find("Date").text)
    Time.append(root.findall("program")[i].findall("concertInfo")[0].find("Time").text)
    program=numpy.column_stack((program,eventType, Venue,Location, Date, Time))
#for j in range(0,len(root.findall("program")[0].findall("worksInfo")[0].findall("work"))-1):
   # workID0.append(root.findall("program")[0].findall("worksInfo")[0].findall("work")[j].get("ID"))
    #composerName0.append(root.findall("program")[0].findall("worksInfo")[0].findall("work")[j].find("composerName").text)
        #workTitle.append(root.findall("./program/worksInfo/work")[1].find("workTitle").text)
        #movement.append(root.findall("./program/worksInfo/work")[1].find("composerName").text)
        #conductorName.append(root.findall("./program/worksInfo/work")[1].find("conductorName").text)
                    #workID.append(work.get("ID"))
            #if work.find("composerName") == None:
            #    composerName.append("NA")
            #else:
            #    composerName.append(work.find("composerName").text)
            #    
            #if work.find("workTitle") == None:
            #    workTitle.append("NA")
            #else:
            #    workTitle.append(work.find("workTitle").text)
            #    
            #if work.find("conductorName") == None:
            #    conductorName.append("NA")
            #else:
            #    conductorName.append(work.find("conductorName").text)
            #if work.find("interval") == None:
            #    interval.append("NA")
            #else:
            #    interval.append(work.find("interval").text)
            #if work.find("movement") == None:
            #    movement.append("NA")
            #else:
            #    movement.append(work.find("movement").text)
        
print program