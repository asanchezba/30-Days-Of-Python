### Day 16 - 30 Days of Python Challenge ###

# Python datetime
import datetime
print(dir(datetime))

''' With dir or help built-in commands it is possible to 
know the available functions in a certain module'''

# Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now) 
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formatting Date Output Using strftime
from datetime import datetime
new_year = datetime(2025, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# String to Time Using strptime
from datetime import datetime
date_string = "2 October, 2024"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# Using date from datetime
from datetime import date
d = date(2024, 1, 1)
print(d)
print('Current date:', d.today())
# date object of today's date
today = date.today()
print("Current year:", today.year)   
print("Current month:", today.month) 
print("Current day:", today.day) 

# Time Objects to Represent Time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print('a =', a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

# Difference Between Two Points in Time Using
today = date(year=2024, month=10, day=6)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2024, month = 10, day = 6, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

# Difference Between Two Points in Time Using timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)