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
''' Sometimes we pass default values to parameters, when we invoke the function.
If we do not pass arguments when calling the function, their default values will be used.'''
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Anna'))

def generate_full_name (first_name = 'Anna', last_name = 'Sánchez'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('Lewis','Hamilton'))

# Arbitrary Number of Arguments
''' If we do not know the number of arguments we pass to our function,
we can create a function which can take arbitrary number of arguments 
by adding * before the parameter name.'''
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) 

# Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Ash','Brook','David','Eyob'))

# Function as a Parameter of Another Function
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))




# Exercicies
# 1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# 2.Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def area_of_circle():
    Pi = 3.14
    r = 34
    area = Pi * r * r
    print(area)
area_of_circle()

# 3.Write a function called add_all_nums which takes arbitrary 
# number of arguments and sums all the arguments. Check if all 
# the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "All arguments must be numbers (int or float)."
print(add_all_nums(2,4,10))

# 4.Temperature in °C can be converted to °F 
# using this formula: °F = (°C x 9/5) + 32. Write a 
# function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celcius_to_fahrenheit(celcius):
    ºF = (celcius * 9/5) + 32
    return ºF
print(convert_celcius_to_fahrenheit(25))

# 5.Write a function called check-season, it takes a month 
# parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
     return('The season is Autum')
    elif month == ' December' or month == 'January' or month == 'February':
     return('The season is Winter')
    elif month == 'March' or month == 'April' or month == 'May':
     return('The season is Spring')
    elif month == 'June' or month == 'July' or month == 'August':
     return('The season is Summer')
    else:
     return('Error, the input must be a month of the year')
print(check_season('April'))

# 6.Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2,4,9,24))

# 7.Quadratic equation is calculated as follows: 
# ax² + bx + c = 0. Write a function which calculates 
# solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a) 
    return x1, x2
print(solve_quadratic_eqn(2,13,5))

# 8.Declare a function named print_list. It takes a 
# list as a parameter and it prints out each element of the list.
def print_list(list):
    for element in list:
        print(element)
print(print_list(['Arsenal', 'FC Barcelona', 'Juventus']))

# 9.Declare a function named reverse_list. It takes an array 
# as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array
print(reverse_list([1, 2, 3, 4, 5]))

# 10.Declare a function named capitalize_list_items. It takes 
# a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    for elements in list:
        return elements.capitalize()
    
bands = ['you me at six', 'mcfly', 'all time low', 'the vamps']
print(capitalize_list_items(bands))

# 11.Declare a function named add_item. It takes a list and an item 
# parameters. It returns a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list
bands = ['you me at six', 'mcfly', 'all time low', 'the vamps']
print(add_item(bands, '5 seconds of summer'))

# 12.Declare a function named remove_item. It takes a list and an item 
# parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    list.remove(item)
    return list
bands = ['you me at six', 'mcfly', 'all time low', 'the vamps']
print(remove_item(bands, 'the vamps'))

# 13.Declare a function named sum_of_numbers. It takes a number parameter 
# and it adds all the numbers in that range.
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(5))

# 14.Declare a function named sum_of_odds. It takes a number parameter and 
# it adds all the odd numbers in that range.
def sum_of_odds(n):
    odds = 0
    for i in range(n+1):
        if i % 2 != 0: 
            odds+=i
    return odds
print(sum_of_odds(5))

# 15.Declare a function named sum_of_even. It takes a number parameter and 
# it adds all the even numbers in that range.
def sum_of_even(n):
    even = 0
    for i in range(n+1):
        if i % 2 == 0: 
            even+=i
    return even
print(sum_of_even(5))

# 16.Declare a function named evens_and_odds. It takes a positive 
# integer as parameter and it counts number of evens and odds in the number.
def even_and_odds(n):
    even = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0: 
            even += i % 2 == 0 
        else: 
            odds += i % 2 != 0
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {even}.")
even_and_odds(100)

# 17.Call your function factorial, it takes a whole number as a parameter
#  and it return a factorial of the number
def factorial(number):
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    return factorial
print(factorial(2))

# 18.Call your function is_empty, it takes a parameter and 
# it checks if it is empty or not
def is_empty(parameter):
    if len(parameter) == 0:
        print('The parameter is empty')
        return True
    else:
        print('The parameter is not empty')
        return False
print(is_empty([]))

# 19.Write different functions which take lists. They should 
# calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    if len(lst) == 0:  # Check if the list is empty to avoid division by zero
        return 0
    mean = sum(lst) / len(lst)  
    return mean
numbers = [1, 0, 2, 6]
print(calculate_mean(numbers))

def calculate_median(lst):
    lst.sort()
    n = len(lst) # Get the length of the list
    
    if n % 2 == 0:
        mid1 = n // 2 - 1  # First middle element index
        mid2 = n // 2      # Second middle element index
        median = (lst[mid1] + lst[mid2]) / 2
    else:
        mid = n // 2      
        median = lst[mid]
    
    print(f'The median is {median}')
calculate_median([1, 23, 95, 14])

from collections import Counter
def calculate_mode(lst):
    c = Counter(lst)
    max_c = max(c.values())
    mode = [key for key, value in c.items() if value == max_c]
    return mode if len(mode) > 1 else mode[0]
print(calculate_mode([2,4,5,2,4,6,1,2]))

def calculate_range(lst):
    max_lst = max(lst)
    min_lst = min(lst)
    range = max_lst - min_lst
    return range
print(calculate_range([1,2,36,92,10]))

# 20.Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    for i in range (2,number):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime(10))

# 21.Write a functions which checks if all items are unique in the list.
def unique(item):
    











     




