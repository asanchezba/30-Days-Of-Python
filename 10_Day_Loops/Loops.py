### Day 10 - 30 Days of Python Challenge ###

# While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue Part 1
''' We use break when we like to get out of or stop the loop'''

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

''' With the continue statement we can skip the current
iteration, and continue with the next'''

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# For Loop
''' For is used for iterating over a sequence (that is either
a list, a tuple, a dictionary, a set, or a string)'''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
     print(number) 

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value) 

# Break and Continue Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

''' The loops stops when it reaches 3'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

''' if the number equals 3, the step after the condition (but inside the loop) is skipped and 
the execution of the loop continues if there are any iterations left.'''

# The Range Function
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# Nested For Loop
person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For Else
''' If we want to execute some message when the loop ends,
we use else'''

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Pass
''' when statement is required (after semicolon), 
but we don't like to execute any code there, we can write the 
word pass to avoid errors. Also we can use it as a placeholder, for future statements.'''

#for number in range(6):
    #pass



# Exercicies
# 1.Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11): 
     print(i)

count = 0
while count <= 10:
    print(count)
    count = count + 1

# 2.Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

count = 11
while count >= 0:
    print(count)
    count = count - 1

# 3.Write a loop that makes seven calls to print(), so we get on the output of a triangle
for i in range(1, 8):  
    print('#' * i)

# 4.Use nested loops to create a pattern with '#'
rows = 8
columns = 8

for i in range(rows):
    for j in range(columns):
        print('#', end=' ')
    # Move to the next line after printing all columns
    print()

# 5. Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

for i in range(11):
    print(i, 'x', i ,'=', i * i)

# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for string in lst:
    print(string)

# 7.Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i %2 == 0:
        print(i)

# 8.Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i %2 != 0:
        print(i)

# 9.Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers is:", total_sum)

# 10.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
total_sum = 0
for i in range(100):
    if i %2 == 0:
        total_sum += i 
    if i %2 != 0:
        total_sum += 1
print("The sum of all evens is:", total_sum)
print("The sum of all odds is:", total_sum)