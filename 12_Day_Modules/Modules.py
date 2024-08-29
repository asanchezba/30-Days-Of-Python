### Day 12 - 30 Days of Python Challenge ###

# Creating a Module
''' To create a module we write our codes in a python script and 
we save it as a .py file.'''

# Importing a Module
import mymodule
print(mymodule.generate_full_name('Anna', 'Sánchez'))

# Import Functions from a Module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Anna','Sánchez'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])

# Import Functions from a Module and Renaming
''' During importing we can rename the name of the module.'''
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Anna','Sánchez'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# Import Built-in Modules
'''We can also import modules by importing the file/function 
using the key word import.'''

# Statistics Module
from statistics import * 
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       
print(median(ages))     
print(mode(ages))       
print(stdev(ages))

# Math Module
import math
print(math.pi)           # pi constant
print(math.sqrt(2))      # square root
print(math.pow(2, 3))    # exponential function
print(math.floor(9.81))  # rounding to the lowest
print(math.ceil(9.81))   # rounding to the highest
print(math.log10(100))   # logarithm with 10 as base

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 
print(sqrt(2))            
print(pow(2, 3))          
print(floor(9.81))       
print(ceil(9.81))         
print(math.log10(100))

'''if we want to import all the function in math module we can use *'''
from math import *

'''we can also rename the name of the function.'''
from math import pi as  PI

