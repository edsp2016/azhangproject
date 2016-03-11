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
rootnode[[1]][["worksInfo"]][[1]][["composerName"]]
xmlToList(rootnode[[1]][["worksInfo"]][[1]][["workTitle"]])


incrementComp <- function(composer_stats, c, season){
  if (is.null(composer_stats[c, season])) {
    composer_stats[c, season] <- 1
  } else if (is.na(composer_stats[c,season])) {
    composer_stats[c, season] <- 1
  } else {
    composer_stats[c, season] <- composer_stats[c, season] + 1
  }
  return(composer_stats)
}

  
composerBySeason <- data.frame()
for (seas in 1:30) {
  firstlist <- xmlToList(rootnode[[seas]])
  season <- firstlist$season
  season <- paste("Season",season,sep=".")
  works <- firstlist$worksInfo
  for (i in 1:length(works)) {
    if (!is.null(works[[i]]$composerName)) {
      composerBySeason <- incrementComp(composerBySeason, works[[i]]$composerName,season)
    }
  }
}


# Parsing the whole thing first is WARNING: SLOW
# xml_aslist <- xmlToList(xmlfile)
# xml_aslist[[22]][["worksInfo"]][[1]][["workTitle"]]