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
