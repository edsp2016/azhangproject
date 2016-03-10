require("XML")

xmlfile <- xmlParse("~/Desktop/1842-43_TO_1910-11.xml")

rootnode = xmlRoot(xmlfile) #gives content of root
class(rootnode)
xmlName(rootnode)
xmlSize(rootnode)

firstchild <- rootnode[[1]]
lastchild <-  rootnode[[1015]]

xmlSize(firstchild) #number of nodes in child
xmlSApply(firstchild, xmlName) #name(s)
xmlSApply(firstchild, xmlSize) #size

rootnode[[1]][["worksInfo"]][[1]][["workTitle"]]
xmlToList(rootnode[[1]][["worksInfo"]][[1]][["workTitle"]])

# Parsing the whole thing first is WARNING: SLOW
# xml_aslist <- xmlToList(xmlfile)
# xml_aslist[[22]][["worksInfo"]][[1]][["workTitle"]]