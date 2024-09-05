### Day 14 - 30 Days of Python Challenge ###

'''In Python functions are treated as first class citizens, allowing you 
to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable'''

# Function as a Parameter
def sum_numbers(nums):  
    return sum(nums)
print(sum_numbers((2,4,3)))

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) 

# Function as a Return Value
def square(x):         
    return x ** 2

def cube(x):            
    return x ** 3

def absolute(x):        
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       
result = higher_order_function('cube')
print(result(3))       
result = higher_order_function('absolute')
print(result(-3))

# Python Closures
'''Closure is created by nesting a function inside another 
encapsulating function and then returning the inner function.'''

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  
print(closure_result(10))  

# Python Decorators
'''A decorator is a design pattern that allows a user to add 
new functionality to an existing object without modifying its 
structure. Decorators are usually called before the definition 
of a function you want to decorate.'''

# Creating Decorators
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g()) 

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

# Applying Multiple Decorators to a Single Function
# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting()) 

# Accepting Parameters in Decorator Functions
