### Day 8 - 30 Days of Python Challenge ###

# Creating a Dictionary
empty_dic = {}
person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
    'skills':['Python', 'Matlab']
}

# Dictionary Lenght
print(len(person))

# Accessing Dictionary Items
print(person['first_name']) 
print(person['country'])    
print(person['skills'])     
print(person['skills'][0])

'''Accessing an item by key name raises an error if the key does not exist. 
To avoid this error first we have to check if a key exist or we can use the get method. 
The get method returns None, which is a NoneType object data type, if the key does not exist.'''

print(person.get('first_name')) 
print(person.get('country'))    
print(person.get('skills')) 
print(person.get('city'))

# Adding Items to a Dictionary
person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
    'skills':['Python', 'Matlab']
}
person['job_title'] = 'Engineer'
person['skills'].append('HTML')

print(person)

# Modifying Items in a Dictionary
person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
    'skills':['Python', 'Matlab']
}
person['first_name'] = 'Bob'
print(person)

# Checking Keys in a Dictonary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) 
print('key5' in dct) 

# Removing Key and Value Pairs from a Dictionary
person = {
    'first_name':'Anna',
    'last_name': 'Sanchez',
    'age':28,
    'country':'Spain',
    'is_married':False,
    'skills':['Python', 'Matlab']
}
person.pop('first_name') # Removes the items with the specified key name
person.popitem() # Removes the last itema
del person['is_married'] # Removes an item with specified key name

print(person)

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # items() changes dictionary to a list of tuples

# Clearing a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())

# Deleting a Dictonary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
