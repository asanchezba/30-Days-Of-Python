# Exercises

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Josh', 'Max', 'Matt', 'Dan']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(country):
    return country.upper()

countries_upper_case = map(change_to_upper, countries)
print(list(countries_upper_case))   

# 2.Use map to create a new list by changing each number to its square in the numbers list
def change_to_square(x):
    return x ** 2

numbers_squared = map(change_to_square, numbers)
print(list(numbers_squared)) 

# 3.Use map to change each name to uppercase in the names list
def change_to_upper(name):
    return name.upper()

names_upper_case = map(change_to_upper, names)
print(list(names_upper_case))  

# 4.Use filter to filter out countries containing 'land'
def land_in_countries(countries):
    if 'land' in countries:
        return True
    return False

land_in_countries = filter(land_in_countries, countries)
print(list(land_in_countries))

# 5.Use filter to filter out countries having exactly six characters
def six_characters(countries):
    if len(countries) == 6:
        return True
    return False

six_characters = filter(six_characters, countries)
print(list(six_characters))

# 6.Use filter to filter out countries containing six letters and more in the country list
def six_or_more_characters(countries):
    if len(countries) >= 6:
        return True
    return False

six_or_more_characters = filter(six_or_more_characters, countries)
print(list(six_or_more_characters))

# 7.Use filter to filter out countries starting with an 'E'
def first_letter(countries):
    if 'E' in countries:
        return True
    return False

first_letter = filter(first_letter, countries)
print(list(first_letter))

# 8.Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))


# 9.Declare a function called get_string_lists which takes a 
# list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

lst = [1, 'hello', 3.14, True, 'world']
string_list = get_string_lists(lst)
print(string_list)

# 10.Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def sum_all(a,b):
    return a + b

print(reduce(sum_all,numbers))

# 11.Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def sentence(countries,string):
    return countries + ', ' + string

result = reduce(sentence, countries) + ' are north European countries'
result = result.replace(', Iceland', ', and Iceland')
print(result)

# 12.Create a function returning a dictionary, where keys stand for starting 
# letters of countries and values are the number of country names starting with that letter.
def count_countries_by_letter(countries):
    letter_count = {}
    
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    
    return letter_count
    
result = count_countries_by_letter(countries)
print(result)
