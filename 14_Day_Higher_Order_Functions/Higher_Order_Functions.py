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
