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

