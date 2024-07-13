### Day 2 - 30 Days of Python Challenge ###

#Build in functions
print(len('Hello world')) #counts the number of characters including space
print(type('Hello world')) #checks data type
number_to_string = str(10) #converts number to string
print(type(number_to_string))
string_to_number = int('10') #converts string to number
print(type(string_to_number))
#input('Enter you name: ') takes users input

#help('keywords') #prints all python reserved words
#help('str') #give info about strings

print(min(20,30,40,50)) #gives the minimum value
print(max(20,30,40,50)) #gives the maximum value
print(min([20,30,40,50])) #it takes a list as an argument and return the min
print(max([20,30,40,50])) #it takes a list as an argument and return the max
print(sum([20,30,40,50])) #it takes only list as an argument and return the sum

#Variables

first_name = 'Anna'
last_name = 'Sánchez'
country = 'Spain'
city = 'Sabadell'
age = 28
is_married = False
skills = ['Matlab', 'Python']
person_info = {
    'firstname': 'Anna',
    'lastname': 'Sánchez',
    'country': 'Spain',
    'city': 'Sabadell'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Anna', 'Sánchez', 'Spain', 28, False
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Casting: converting one data type to another type

# int to float
num_int = 10
print('num_int',num_int)         
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)                  
num_str = str(num_int)
print(num_str) 

# str to int or float
num_str = '10.6'
#print('num_int', int(num_str))      
print('num_float', float(num_str))

# str to list
first_name = 'Anna'
print(first_name)              
first_name_to_list = list(first_name)
print(first_name_to_list)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

import math
radius = 30
area_of_circle = math.pi * radius ** 2 
circum_of_circle = 2 * math.pi * radius
#radius = int(input('Enter radius: '))
area_of_circle = math.pi * radius ** 2 

print(area_of_circle)
print(circum_of_circle)


