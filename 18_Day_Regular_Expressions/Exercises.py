import re 

# 1. What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not 
love something which can give you all the capabilities to develop an application what else can you love.'''

# Extract words from the paragraph
words = re.findall(r'\b\w+\b', paragraph)

# Count word frequencies using a dictionary
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort and format the output
output = sorted([(count, word) for word, count in word_counts.items()], key=lambda x: (-x[0], x[1]))

print(output)

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in 
# the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these 
# numbers from this whole text and find the distance between the two furthest particles.
text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in 
the negative direction, 0 at origin, 4 and 8 in the positive direction.'''

# Extract numbers from text
points = re.findall(r'-?\d+', text)

# Convert extracted strings to integers
points = list(map(int, points))

# Find the minimum and maximum positions
min_point = min(points)
max_point = max(points)

# Calculate the distance between the two furthest particles
distance = abs(max_point - min_point)

print('Points = ', points)
print('Distance = ', distance)

# 3. Write a pattern which identifies if a string is a valid python variable
