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

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include itesm from index 3 to last
orange_to_the_rest = fruits[-3:]

# Changing Tuples to Lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple' # Tuple is immutable if we want to modify a tuple we should change it to a list
print(fruits)    
fruits = tuple(fruits)
print(fruits)    

# Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False

# Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits # It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself 

