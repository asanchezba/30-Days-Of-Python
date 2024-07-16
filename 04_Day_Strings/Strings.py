### Day 4 - 30 Days of Python Challenge ###

my_string = 'This is a string'
my_other_string = '''This is a multiline string '''
print(my_string)
print(my_other_string)

# String concatenation #
first_name = 'Anna '
last_name = 'Sánchez'
full_name = first_name + last_name
print(full_name)

# Escape sequences #

# \n: new line
# \t: tab (8 spaces)
# \\: back slash
# \': single quote
# \'': double quote

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') 
print('Days\tTopics\tExercises') 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') 
print('In every programming language it starts with \"Hello, World!\"')

# String formating #

# %s: string
# %d: integers
# %f: floating point numbers
# '%.number of digistsf': floating point numbers with fixed precision

first_name = 'Anna'
last_name = 'Sánchez'
language = 'Python'
formated_string = 'I am %s %s. I learn %s' %(first_name, last_name, language)
print(formated_string)

first_name = 'Anna'
last_name = 'Sánchez'
language = 'Python'
formated_string = 'I am {} {}. I learn {}' .format(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d i %.2f.' %(radius, area)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) 
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


