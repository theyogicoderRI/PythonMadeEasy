##import datetime
##from datetime import date, datetime
##timer = date(2018,12,31)
##print(timer)
###output- 2018-12-31
##
### this prints out the day of the week it is
##day = timer.weekday()
##if day == 0:
##    print("Today is Monday: " , day)
### output:  Today is Monday:  0   
##    
### this prints out the weekday it is
##wkday = timer.isoweekday()
##if timer.isoweekday():
##    print("Today is a weekday! And: ", wkday, " Is a Monday")
### output: Today is a weekday! And:  1 , Is a Monday


from datetime import date
##### what is today?
##today = date.today()
##print(today)
##month = today.month
##print(month)
##year = today.year
##print(year)
##day = today.day
##print(day)




###How many days was Halloween (10/31/2018)?
##
##today = date.today()
##hw = date(2018,10,31)
##print(("Halloween was: {0} days ago".format((today -hw).days)))
##
###FIRST GET TODAY
##t = date.today()
##print(t)
##
### THEN GET THE YEAR
##y = t.year
##print(y)
##
### THEN GET THE MONTH
##m = t.month
##print(m)
##
### THEN GET THE DAY
##d = t.day
##print(d)
##

##from datetime import date
### diff between 2 dates
##d1 = date(2019,1,2)
##d2 = date(2018,12,31)
##diff = d1 - d2  # d1 wil always be the most recent date- Think bigger number
##diff2 = d2 -d1
##print(diff)
##print(abs(diff))
####
##
##
### EXAMPLE OF COUNTING DAYS TO AN EVENT ***********
import time
from datetime import date
today = date.today()
print(today)

my_bonus = date(today.year, 2, 15)
if my_bonus < today:
    my_bonus = my_bonus.replace(year = today.year + 1)
print(my_bonus)
time_to_bonus = abs(my_bonus - today)
print("Your bonus comes in: ", time_to_bonus.days, 'days. :)')
