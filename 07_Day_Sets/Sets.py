### Day 7 - 30 Days of Python Challenge ###

# Creating a Set
empty_set = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's Length
print(len(fruits))

# Checking an Item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits )

# Adding Items to a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables) # to add multiple items to a set
print(fruits)

