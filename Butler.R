rm(list = ls())
if(!"EnvStats" %in% installed.packages()){install.packages("EnvStats")}
library(EnvStats)
PER <- c(29,40,46,15,14,40,36,24,33,30,33,36,30,35,30,38,20,37,29,20,14,33,26,19,26,16,28,19,21,20,26,24,17,29,21,30,36,20,31,35,22,30) #this was the values of Butler's PER rating throughout the regular season
shapiro.test(PER)
hist(PER,col="light blue",las=1)
