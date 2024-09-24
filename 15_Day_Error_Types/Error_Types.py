### Day 15 - 30 Days of Python Challenge ###

# SyntaxError
#print 'hello world'
print('hello world')

# NameError
#print(age) # NameError: name 'age' is not defined
age = 28
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
#numbers[5] #IndexError: list index out of range

# ModuleNotFoundError
#import maths #ModuleNotFoundError: No module named 'maths'
import math 

# AttributeError
import math 
#math.PI #AttributeError: module 'math' has no attribute 'PI'
math.pi

# KeyError
users = {'name':'Anna', 'age':28, 'country':'UK'}
users['name']
#users['county'] #KeyError: 'county'
users = ['country']

# TypeError
#4 + '3' #TypeError: unsupported operand type(s) for +: 'int' and 'str'
4 + int('3')
4 + float('3')

# ImportError
#from math import power # ImportError: cannot import name 'power' from 'math' 
from math import pow
pow(2,3)

# ValueError
#int('12a') # ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError
#1/0 # ZeroDivisionError: division by zero






