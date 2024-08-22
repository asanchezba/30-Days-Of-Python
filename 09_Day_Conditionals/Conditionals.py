### Day 9 - 30 Days of Python Challenge ###

# If Condition
''' If is used to check if a condition is true and to execute the block code.'''

a = 3
if a > 0:
    print('A is a positive number')

# If Else 
''' If condition is true the first block will be executed, if not the else condition 
will run.'''

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else
''' We use elif when we have multiple conditions.'''

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

''' We can avoid writing nested condition by using logical operator and.'''

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')



# Exercicies
# 1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = input('Enter your age: ')
X = 18 - int(age)
if int(age) >= 18:
     print('You are old enough to drive.')
else:
     print('You need', X, 'more years to learn to drive.')

# 2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 
# 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 28
your_age = input('Enter you age: ')
difference = my_age - int(your_age)

if my_age >= int(your_age):
     if difference > 0:
          print('I am', difference, 'years older than you')
     elif difference == 1:
        print('I am', difference, 'year older than you')
     elif difference == 0:
        print('We are the same age')
else:
     print('You are', abs(difference), 'years older than me')

