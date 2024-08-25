### Day 11 - 30 Days of Python Challenge ###

# Declaring and Calling a Function
def function_name():
    'codes'

function_name()

# Function Without Parameters
def generate_full_name():
    first_name = 'Anna'
    last_name = 'Sánchez'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()

# Function Returning a Value - Part 1
def generate_full_name():
    first_name = 'Anna'
    last_name = 'Sánchez'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())

# Function with Parameters
''' In a function we can pass different data 
types (number, string, boolean, list, tuple
dictionary or set) as a parameter'''

''' Single Parameter: if our function takes a
parameter we should call our function with an argument'''
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Anna'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

''' Two Parameter: a function may or may not have a parameter
or parameters. A function may also have two or more parameters.'''
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Anna', 'Sánchez'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2024, 1995))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# Passing Arguments with Key and Value
''' If we pass the arguments with key and value, the order of the
arguments does not matter'''
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(lastname = 'Sánchez', firstname = 'Anna'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2))

# Function Returning Value - Part 2
''' If w do not return a value with a function, our function is returing
a None by default. To return a value with a function we use the keyword
raturn followed by the variable we are returning.'''
def print_name(firstname):
    return firstname
print_name('Anna')

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Anna', lastname='Sánchez')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2024, 1995))

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) 
print(is_even(7))

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Functions with Default Parameters



