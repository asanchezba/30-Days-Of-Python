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

print(3 > 2 and 4 > 3) 
print(3 > 2 and 4 < 3) 
print(3 < 2 and 4 < 3) 
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  
print(3 > 2 or 4 < 3)  
print(3 < 2 or 4 < 3)  
print('True or False:', True or False)
print(not 3 > 2)     
print(not True)      
print(not False)     
print(not not True)  
print(not not False) 


# Exercicies #

age = 28
height = 167.0
complex_number = 4 + 3j 

#Area of a triangle
#base = input('Enter base:')
#height = input('Enter height:')
#print('The area of the triangle is', 0.5*int(base)*int(height))

#Perimeter of a triangle
#side_a = input('Enter side a:')
#side_b = input('Enter side b:')
#side_c = input('Enter side c:')
#print('The perimeter of the triangle is', int(side_a)*int(side_b)*int(side_c))

#Area and perimeter of a rectangle
#length = input('Enter lenght:')
#width = input('Enter width:')
#print('The area of the rectangle is', int(length)*int(width), 'and the perimeter is', 2*int(length)+int(width))

#Radius and circumference of a circle
from math import pi as PI
#radius = input('Enter radius:')
#area = PI * int(radius) ** 2
#circumference = 2 * PI * int(radius)
#print('The area of the circle is', area, 'and the cirfumference is', circumference)

import math

# Coefficients of the quadratic equation
a = 1
b = 6
c = 9

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # Calculate the two possible roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print(f"The roots of the equation are: {root1} and {root2}")
else:
    print("The equation has no real roots.")


print(len('python') == len('dragon'))
print('on' in ('python' and 'dragon'))
print('jargon' in 'I hope this course is not full of jargon')
len_pyth = len('pyton')
len_pyth_float = float(len_pyth)
len_pyth_str = str(len_pyth_float)
print(len_pyth_float)
print(len_pyth_str)

#Check if a number is even
#number = int(input('Enter a number:'))
#if number % 2 == 0:
    #print('This number is even')
#else:
   # print('This number is odd')


print(7//3 == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)

def display_table():
    
    # Iterate through the rows
    for i in range(1, 6):
        value1 = 1
        value2 = i
        value3 = i ** 2
        value4 = i ** 3
        
        # Print the values in a formatted way
        print(f"{i:<6} {value1:<6} {value2:<6} {value3:<6} {value4:<6}")

# Call the function to display the table
display_table()
