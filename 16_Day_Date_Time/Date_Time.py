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