# timedelta

from datetime import timedelta, datetime, date
##print(timedelta(days=365))
##print("today is: " + str(datetime.now()))
##print("30 days from day will be:" + str(datetime.now() + timedelta(days=30)))
##print("60 days from day will be:" + str(datetime.now() + timedelta(days=60)))
##print("90 days ago was: " + str(datetime.now() - timedelta(days=90)))
##today = date.today()
##hw = date(2018,10,31)
##diff= (today - hw.days)
##print("How many days between today and last halloween? ", )


#How many days was Halloween (10/31/2018)?

today = date.today()
hw = date(2018,10,31)
print(("Halloween was: {0} days ago".format((today -hw).days)))

# how many seconds are in a year?
year = timedelta(days=365)
print("There are {0} seconds in a year. Use them wisely" \
      .format(year.total_seconds()))

# how many days in 5 years?
print( "How many days in 5 years: ", (5 *year).days)
