# Exercises - Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# === LEVEL 1 ===

# Find the length of the set it_companies
len(it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Instagram', 'TikTok', 'Uber'])

# Remove one of the companies from the set it_companies
it_companies.remove('Amazon')

# What is the difference between remove and discard
# remove() will remove the item but if it's not found it will raise errors, discard() doesn't

# === LEVEL 2 ===

# Join A and B
C = A.union(B)

# Find A intersection B
D = A.intersection(B)

# Is A subset of B
is_subset = A.issubset(B)

# Are A and B disjoint sets
is_disjoint = A.isdisjoint(B)

# Join A with B and B with A
E = A.union(B)
F = B.union(A)

# What is the symmetric difference between A and B
# Returns a set that contains items from both groups, except the ones that are in both groups [(A/B) U (B/A)]

# Delete the sets completely
del A
del B

# === LEVEL 3 ===

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)

# "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
split_phrase = slice()
unique_words = set(split_phrase)
print('This many words are unique -> ', len(unique_words))

# Explain the difference between the following data types: string, list, tuple and set
# String -> collection of characters put altogether
# List -> interchangable array which you can access to through indexes and for loops
# Tuple -> unmodifiable array, that you can access to through indexes and for loops. You cannot add or remove items in a tuple
# Set -> List of unique items, that you can access to through for loops. You can add and remove items (append) 