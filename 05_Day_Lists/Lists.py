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