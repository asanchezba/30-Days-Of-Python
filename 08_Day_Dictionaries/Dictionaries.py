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
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys) 

# Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)



#Exercicies
# 1.Create an empty dictionary called dog
dog = {}

# 2.Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Roscoe'
dog['colour'] = 'Brown'
dog['breed'] = 'Bulldog'
dog['legs'] = 4
dog['age'] = 11
print(dog)

# 3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Anna',
    'last_name': 'Sánchez',
    'gender': 'female',
    'age': 28,
    'marital_status': 'not married',
    'skills': ['Python', 'Matlab'],
    'country': 'Spain',
    'city': 'Barcelona'
}

# 4.Get the length of the student dictionary
print(len(student))

# 5.Get the value of skills and check the data type, it should be a list
student = {
    'first_name': 'Anna',
    'last_name': 'Sánchez',
    'gender': 'female',
    'age': 28,
    'marital_status': 'not married',
    'skills': ['Python', 'Matlab'],
    'country': 'Spain',
    'city': 'Barcelona'
}
skills = student.get('skills')
print(type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
student['skills'].append('JavaScript')
print(student)

# 7.Get the dictionary keys as a list
keys = student.keys()
print(keys) 

# 8.Get the dictionary values as a list
values = student.values()
print(values)

# 9.Change the dictionary to a list of tuples using items() method
print(student.items())

# 10.Delete one of the items in the dictionary
student = {
    'first_name': 'Anna',
    'last_name': 'Sánchez',
    'gender': 'female',
    'age': 28,
    'marital_status': 'not married',
    'skills': ['Python', 'Matlab'],
    'country': 'Spain',
    'city': 'Barcelona'
}

del student['city']

# 11.Delete one of the dictionaries
del student

