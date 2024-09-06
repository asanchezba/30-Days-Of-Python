# Exercises

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Josh', 'Max', 'Matt', 'Dan']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(name):
    return name.upper()

countries_upper_case = map(change_to_upper, countries)
print(list(countries_upper_case))   

# 2.Use map to create a new list by changing each number to its square in the numbers list
