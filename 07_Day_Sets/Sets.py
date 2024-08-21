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

# Removing Item from a Set
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

# Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)

# Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))

# Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     
print(dragon.difference(python))

# Finding Symmetric Difference Between Two Sets
'''It returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)'''

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

# Joint Sets
'''If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.'''

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}



# Exercicies
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.Find the length of the set it_companies
print(len(it_companies))

# 2.Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3.Insert multiple IT companies at once to the set it_companies
additional_companies = {'SAP', 'Juniper', 'Git', 'bmc', 'ebay', 'PayPal'}
it_companies.update(additional_companies)
print(it_companies)

# 4.Remove one of the companies from the set it_companies
it_companies.remove('bmc')
print(it_companies)

# 5.Join A and B
print(A.union(B))

# 6.Find A intersection B
print(A.intersection(B))

# 7.Is A subset of B
print(A.issubset(B))

# 8.Are A and B disjoint sets
print(A.isdisjoint(B))

# 9.What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 10.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age_set))
print(len(age))

# 11.Delete the sets completely
del A, B, it_companies

