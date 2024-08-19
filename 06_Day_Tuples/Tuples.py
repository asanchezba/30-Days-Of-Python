### Day 6 - 30 Days of Python Challenge ###

# Creating a Tuple
empty_tuple = ()
tpl = ('item1', 'item2', 'item3')
print(len(tpl))

# Accessing Tuple Items
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_index =len(fruits) - 1
print(last_index)
last_fruit = fruits[last_index]
print(last_fruit)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
print(first_fruit)
second_fruit = fruits[-3]
print(second_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Slicing tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
print(all_fruits)
all_fruits= fruits[0:]      # all items
print(all_fruits)
orange_mango = fruits[1:3]  # doesn't include itesm from index 3 to last
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)