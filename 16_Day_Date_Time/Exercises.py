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
