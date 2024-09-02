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

# Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive



# Exercicies
# 1.Writ a function which generates a six digit/character random_user_id
import random 
def random_user_id():
    length_of_string = 8
    sample_str = "abcdefghijklmnopqrstuvwxyz0123456789"
    generated = ''.join(random.choices(sample_str, k = length_of_string))
    return generated
print(random_user_id()) 

# 2.Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the 
# number of IDs which are supposed to be generated.
import random
def user_id_gen_by_user():
    print('Enter number of id: ')
    number_of_id = int(input())  # Convert input to integer
    print('Enter number of characters: ')
    number_of_char = int(input())  # Convert input to integer
    
    sample_str = "abcdefghijklmnopqrstuvwxyz0123456789"
    generated_ids = []  # List to store all generated IDs
    
    for i in range(number_of_id):
        generated = ''.join(random.choices(sample_str, k=number_of_char))
        generated_ids.append(generated)  # Add each generated ID to the list
    
    return generated_ids

generated_ids = user_id_gen_by_user()
for user_id in generated_ids:
    print(user_id)

# 3.Write a function named rgb_color_gen. It will generate rgb colors 
# (3 values ranging from 0 to 255 each).
import random
def rgb_color_gen():
    generated_color = []
    for i in range(3):  # Loop three times, once for each color component
        generated = random.randint(0, 255)  # Generate a random integer between 0 and 255
        generated_color.append(generated)
    print(f'rgb({generated_color})')
print(rgb_color_gen())

# 4.Write a function list_of_hexa_colors which returns any number of hexadecimal 
# colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral 
# system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.

def list_of_colors():
    sample = 'abcdef0123456789'
    generated_color = ''.join(random.choices(sample, k = 6))
    print(f'#{generated_color}')
print(list_of_colors())

# 5.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n=1):
    generated_rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        generated_rgb_colors.append((r, g, b))
    return generated_rgb_colors
print(list_of_rgb_colors(5))

# 6.Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type,number):
    sample = 'abcdef0123456789'
    generated_rgb_colors = []
    generated_hexa_colors = []
    
    for i in range(number):
     if type == 'rgb':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        generated_rgb_colors.append(f'rgb({r, g, b})')
        
     elif type == 'hexa':
         generated_color = ''.join(random.choices(sample, k = 6))
         generated_hexa_colors.append(f'#{generated_color}')

    if type == 'rgb':
        return generated_rgb_colors
    elif type == 'hexa':
        return generated_hexa_colors
    else:
        return []

print(generate_colors('hexa',4))
print(generate_colors('rgb',2))

