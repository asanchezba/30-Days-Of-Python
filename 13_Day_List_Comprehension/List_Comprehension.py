### Day 13 - 30 Days of Python Challenge ###

# List Comprehension
'''Compact way of creating a list from a sequence. It is 
a short way to create a new list. List comprehension is 
considerably faster than processing a list using the for loop'''

# syntax
#[i for i in iterable if expression]

# Example 1: Change a string to a list of characters

# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst) 

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)

# Example 2: Generate a list of numbers

numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers) 

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares) 

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers) 

# Example 3: List comprehension combined with if expression

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers) 

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers) 

# Filter numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) 

# Lambda Function
'''A small anonymous function without a name. 
It can take any number of arguments, but can only have one expression.'''


