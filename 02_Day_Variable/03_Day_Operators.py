### Day 3 - 30 Days of Python Challenge ###

# Arithmetic Operations in Python
# Integers
print('Addition: ', 1 + 2)        
print('Subtraction: ', 2 - 1)     
print('Multiplication: ', 2 * 3)  
print ('Division: ', 4 / 2)       # Division in Python gives floating number
print('Division: ', 6 / 2)          
print('Division: ', 7 / 2)        
print('Division without the remainder: ', 7 // 2)   # Gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   
print('Modulus: ', 3 % 2)         # Gives the remainder
print('Exponentiation: ', 2 ** 3) 

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Declaring the variables
a = 3
b = 2

# Arithmetic operations and assigning the result to a variable
total = a + b # Sum is a built-in function - try to avoid overriding built-in functions
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

import math
# Calculating area of a circle
radius = 10
area_of_circle = math.pi * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81 
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print('Density:', density)


# Comparison Operators #

print(3 > 2)    
print(3 >= 2)    
print(3 < 2)     
print(2 < 3)     
print(2 <= 3)    
print(3 == 2)    
print(3 != 2)    
print(len('mango') == len('avocado'))  
print(len('mango') != len('avocado'))  
print(len('mango') < len('avocado'))   
print(len('milk') != len('meat'))      
print(len('milk') == len('meat'))      
print(len('tomato') == len('potato'))  
print(len('python') > len('dragon'))   

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Anna', 'A' in 'Anna')
print('B in Anna', 'B' in 'Anna')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is 2 ** 2)


# Logical Operators #
