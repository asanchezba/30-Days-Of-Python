### Day 5 - 30 Days of Python Challenge ###

# Lists #

my_list = list()
my_other_list = []

fruits = ['banana', 'mango', 'apple', 'kiwi']
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))

# Accessing list items
first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Unpacking list items
first_fruit, second_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(rest)

# Slicing items from a List
all_fruits = fruits[0:4] # it returns all the fruits
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)
mango_and_apple = fruits[1:3] # it does not include the first index
print(mango_and_apple)
mango_apple_kiwi = fruits[1:]
print(mango_apple_kiwi)
banana_and_apple = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item
print(banana_and_apple)

# Modifying lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Adding Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# Inserting Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)        
fruits.insert(3, 'lime')   # insert lime between apple and mango
print(fruits)

# Removing Items for a List
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana') # removes the first occurrence of the item in the list
print(fruits) 
fruits.remove('lemon')
print(fruits)

# Removing Items Using Pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop() # removes the last item if index is not specified
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using Del
fruits = ['banana', 'organge', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
#del fruits # delets the list completely
#print(fruits)

# Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)