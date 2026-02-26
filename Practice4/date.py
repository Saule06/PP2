#1
from datetime import datetime, timedelta

today = datetime.now()
result = today - timedelta(days=5)

print(result)

#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print(without_microseconds)

#4
from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)