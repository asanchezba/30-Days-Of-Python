# 1.Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
print(now) 
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute 
print(f'{day}/{month}/{year}, {hour}:{minute}')

# 2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)

# 3.Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4.Calculate the time difference between now and new year.
from datetime import date
today = date(year=2024, month=10, day=6)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# 5.Calculate the time difference between 1 January 1970 and now.
from datetime import timedelta
past = timedelta(weeks=1, days=1)
now = timedelta(weeks=10, days=6)
time_difference = now - past
print('Time difference: ', time_difference)