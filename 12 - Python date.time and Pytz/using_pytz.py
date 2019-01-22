# using the pytz module
'''pytz brings the Olson tz database into Python.
This library allows accurate and cross platform
timezone calculations using Python 2.4 or higher.
It also solves the issue of ambiguous times at the
end of daylight saving time, which you can read
more about in the Python Library Reference (datetime.tzinfo).'''

from datetime import datetime, timedelta
from datetime import datetime, timedelta
import pytz
utc = pytz.utc
eastern = timezone('US/Eastern')
print(eastern)
