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
