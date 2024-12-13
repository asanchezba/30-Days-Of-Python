### Day 18 - 30 Days of Python Challenge ###

'''A regular expression or RegEx is a special text string 
that helps to find patterns in data. A RegEx can be used to 
check if some pattern exists in a different data type. To use RegEx 
in python first we should import the RegEx module which is called re.'''

import re

# Methods in re Module

''' To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string'''

# Match
# syntac
'''re.match(substring, string, re.I)'''
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore


txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I) 
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# Search
# syntax
'''re.match(substring, string, re.I)'''
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)

# Searching for All Matches Using findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('language', txt, re.I)
print(matches)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('python', txt, re.I) #using re.I both lowercase and uppercase letters are included
print(matches)

# Replacing a Substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)
# alternative
#match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
#print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

# Writing RegEx Patterns
