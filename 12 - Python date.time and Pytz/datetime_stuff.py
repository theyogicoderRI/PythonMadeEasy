import datetime
from datetime import date, datetime
## 
##x = datetime.MINYEAR
##print("The earliest year allowed in this module is: ", x)
##
##y = datetime.MAXYEAR
##print("The latest year allowed in this module is: ", y)
##
##

import datetime
from datetime import date, datetime
timer = date(2018,12,31)
print(timer)
#output- 2018-12-31

# this prints out the day of the week it is
day = timer.weekday()
if day == 0:
    print("Today is Monday: " , day)
# output:  Today is Monday:  0   
    
# this prints out the weekday it is
wkday = timer.isoweekday()
if timer.isoweekday():
    print("Today is a weekday! And: ", wkday, " Is a Monday")
# output: Today is a weekday! And:  1 , Is a Monday

# returns year, week and weekday
cal = timer.isocalendar()
print(cal)
# output: (2019, 1, 1)
# iso_week is the first week of the year that contains a Thursday- this is week 1
# that is why it is 2019- the Tursday is in 2019
# iso_weekday is the day of the week where Monday is 1

# returns ISO format
iso = timer.isoformat()
print(iso)
###output- 2018-12-31
##
##ctimer = timer.ctime()
##print(ctimer)
# output: Mon Dec 31 00:00:00 2018

#The program below converts a datetime object containing current date
#and time to different string formats.
#timer = date(2018,12,31)
##day = timer.strftime("%A")
##print("today is: ",day)
##
##day_ab = timer.strftime("%a")
##print("today is: ",day_ab)
##
##year = timer.strftime("%Y")
##print("The year is: ", year)
##
##year_2 = timer.strftime("%y")
##print("The year is: ", year_2)
##
##month = timer.strftime("%B")
##print("The month is: ", month)
##
##month_ab = timer.strftime("%b")
##print("The month is: ", month_ab)
##
##month_num = timer.strftime("%m")
##print("The month is: ", month_num)

####clock_set = timer.strftime("%I")
####print("The clock is: ", str(clock_set) + "hr time")
####
####clock_set_24 = timer.strftime("%H")
####print("The clock is: ", str(clock_set_24) + "hr time")
##
##tz = timer.strftime("%Z")
##print("The timezone here is: ", tz)
### if not set returns nothing


####locale = timer.strftime("%p")
####print("Here it is : ", locale)


##today = date.today()
###output- 2018-12-31
##
##right_now = datetime.now()
##print(right_now)
### output: 2018-12-31 16:34:59.336646
##
### use datetime.now() to get the year
##year_2018 = right_now.year
##print(year_2018)
##
### get just the year from timer variable (date)
##month = timer.month
##print(month)
##
### get just the month
##year = timer.year
##print(year)
##
### get just the day
##day = timer.day
##print(day)

##now = datetime.now()
##my_bday = datetime(1968,1,17)
##
##
##timestamp = datetime.timestamp(my_bday)
##print("timestamp =", timestamp)
##date_time = datetime.fromtimestamp(timestamp)
##
##print("Date time object:", date_time)
##
##d = date_time.strftime("%d %B, %Y")
##print("Output 4:", d)
##
##I_was_born = my_bday.strftime("%A")
##print("I was born on a: ", I_was_born )
##
##dec_17 = datetime(2018,12,17)
##dec_17_was = dec_17.strftime("%A")
##print("Dec 17th was a: ", dec_17_was )

# the differnece between 2 date
##orig_date = date(2018, 11, 30)
##now = date(2018,12,31)
##diff = (now - orig_date)
##print(diff.days)

# what was the date 100 days ago ? - Timedelta function
##from datetime import timedelta
##right_now = datetime.now()
##what_date = right_now - timedelta(days = 100)
##print(what_date)
##
### convert this date to month and day only
##print( str(what_date.month)+ "/" + str(what_date.day))


 # How is this timedelta??????
 #A timedelta object represents a duration, the difference between two dates or times
##datetimeFormat = '%Y-%m-%d'

##date1 = '2018-12-31'
##date2 = '2018-6-30'
##diff = datetime.strptime(date1, datetimeFormat)\
##    - datetime.strptime(date2, datetimeFormat)
##print("Days:", diff.days)
##print("Weeks:", (round(diff.days/7, 1)))
##print("Months:", (round(diff.days/30,1)))

# converting from a date in string format to datetime using strptime
datetimeFormat = '%B %d, %Y'
string_date = datetime.strptime('June 25, 2019', datetimeFormat )
print(string_date)
 
### what is today?
today = date.today()
print(today)
month = today.month
print(month)
year = today.year
print(year)
day = today.day
print(day)

# print day of the week. Monday is 0
weekday = today.weekday()
print(weekday)

# use datetime:
whole_thing = datetime.now()
print(whole_thing)

# just the time please:
current_t = datetime.time(datetime.now())
print(current_t)

#print out 12 hour time it is now:
now = datetime.now()
print(now.strftime("%I:%M  %p"))

#print out 24 hour time it is now:
print(now.strftime("%H:%M"))

# timedelta:::

from datetime import timedelta
print(timedelta(days=365))
print("today is: " + str(datetime.now()))
print("30 days from day will be:" + str(datetime.now() + timedelta(days=30)))
print("60 days from day will be:" + str(datetime.now() + timedelta(days=60)))

##
###How many days was Halloween (10/31/2018)?
##
##today = date.today()
##hw = date(2018,10,31)
##print(("Halloween was: {0} days ago".format((today -hw).days)))
##
### how many seconds are in a year?
##year = timedelta(days=365)
##print("There are {0} seconds in a year. Use them wisely" \
##      .format(year.total_seconds()))
##
### how many days in 5 years?
##print( "How many days in 5 years", (5 *year).days)

### FIRST GET TODAY
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
### diff between 2 dates
##d1 = date(2019,1,1)
##d2 = date(2018,12,31)
##diff = d1 - d2  # d1 wil always be the most recent date- Think bigger number
##print(diff)
##
### find date differenece using timedelta
##from datetime import timedelta
##td1 = timedelta(days = 365)
##td2 = timedelta(days = 90)
### get 365 or 1 year before a specified date (2018,12,31)
##d3 = d2 - td1
##print(d3)
### get 90 days before a specified date (2018,12,31)
##d4 = d2 -td2
##print(d4)
##
### get 9- days from a given date
##d5 = d2 + td2
##print(d5)
##
### determine which daty of the week  a specified date is (Monday is 0)
##is_wd = d5.weekday()
##print(is_wd)
##
### use iso caledar on a given date to return ISO year, ISO weeknumber and ISO weekday 2019-03-31
##print(d5.isocalendar())
### output: (2019, 13, 7)
### year = 2019
### week = 13 last week of march)
###weekday = 7 (sunday)
##
###print the ISO 8601 string format
##print(d5.isoformat())
##
### print a string using ctime- platofrms where native C ctime() function conforms to c standard
##print(d5.ctime())


# EXAMPLE OF COUNTING DAYS TO AN EVENT ********************************

##import time
##from datetime import date
##today = date.today()
##print(today)
##
##my_bonus = date(today.year, 2, 15)
##if my_bonus < today:
##    my_bonus = my_bonus.replace(year = today.year + 1)
##print(my_bonus)
##time_to_bonus = abs(my_bonus - today)
##print(time_to_bonus.days)
    

# NOW WORKING WITH datetime*****************************
##
###current local date and time
##from datetime import datetime, tzinfo, timedelta
##to_day = datetime.today()
##print(to_day)
##
### may be the exact same as today() if tz = None
##now = datetime.now()
##print(now)
##
###Return the current UTC date and time
###UTC is the time standard commonly used across the world. 
##utc = to_day.utcnow()
##print(utc)
##
### return just the date from datetime
##print(to_day.date())
##
### return just the time from datetime
##print(to_day.time())
##
### return a full time stamp in a tuple form including year, m, d, h, m,s, weekday, etc
##print(to_day.timetuple())
##
### return the  iso calendar tuple of year, week number and weekday
##print(to_day.isocalendar())
##
###Return a string representing the date and time in ISO 8601 format
##print(to_day.isoformat())
##
##print(to_day.timetz())
##print(to_day.tzname())
##
##from time import gmtime, strftime
##print(strftime("%z", gmtime()))
##print(strftime("%z +0000", gmtime()))
##
###Return the local date corresponding to the POSIX timestamp
##print(to_day.timestamp())


