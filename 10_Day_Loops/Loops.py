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
