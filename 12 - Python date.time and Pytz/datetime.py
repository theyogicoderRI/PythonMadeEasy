import datetime
from datetime import date, datetime

##today = datetime.today()
##now = datetime.now()
##my_bday = datetime(1999,5,18)
##my_bday_old = datetime(1939,5,18)
##print(my_bday)
##print(my_bday_old)

##
##my_bday = datetime(1999,5,18)
##timestamp = datetime.timestamp(my_bday)
##print("timestamp =", timestamp)
##date_time = datetime.fromtimestamp(timestamp)
##
##print("Date time object:", date_time)
##
##d = date_time.strftime("%d %B, %Y")
##print("Bday from timestamp:", d)
##
##I_was_born = my_bday.strftime("%A")
##print("I was born on a: ", I_was_born )
##
##dec_17 = datetime(2018,12,17)
##dec_17_was = dec_17.strftime("%A")
##print("Dec 17th was a: ", dec_17_was )



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

from datetime import datetime, tzinfo, timedelta
to_day = datetime.today()
#Return the current UTC date and time
#UTC is the time standard commonly used across the world. 
utc = to_day.utcnow()
print(utc)

# return just the date from datetime
print(to_day.date())

# return just the time from datetime
print(to_day.time())

# return the  iso calendar tuple of year, week number and weekday
print(to_day.isocalendar())

#Return a string representing the date and time in ISO 8601 format
print(to_day.isoformat())


##
##from time import gmtime, strftime
##print(strftime("%z", gmtime()))
##print(strftime("%z +0000", gmtime()))
##print(to_day.timetz())
##print(to_day.tzname())
# return a full time stamp in a tuple form including year, m, d, h, m,s, weekday, etc
print(to_day.timetuple())
###Return the local date corresponding to the POSIX timestamp
##print(to_day.timestamp())
