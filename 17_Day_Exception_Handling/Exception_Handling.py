### Day 17 - 30 Days of Python Challenge ###

# Exception Handling
try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# Packing and Unpacking Arguments in Python
'''We use two operators:
* for tuples
** for diccionaries'''

# Unpacking lists
#def sum_of_five_nums(a, b, c, d, e):
    #return a + b + c + d + e

#lst = [1, 2, 3, 4, 5]
#print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) #15

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers) 

'''A list or a tuple can also be unpacked like this: '''
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

# Unpacking Dictionaries



