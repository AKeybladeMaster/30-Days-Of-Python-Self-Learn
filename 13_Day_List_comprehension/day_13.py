# Exercises - Day 13

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([number for number in numbers if number <= 0])

# Flatten the following list of lists of lists to a one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([number for row in list_of_lists for number in row])

# Using list comprehension create the following list of tuples (check image on MD file)
print([tuple([number] + [number ** power for power in range(6)]) for number in range(11)])

# Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries])

# Change the following list (countries) to a list of dictionaries
print([{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries])

# Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([f'{first} {last}' for [(first, last)] in names])

# Write a lambda function which can solve a slope or y-intercept of linear functions
# y = mx + b: return either slope or y-intercept.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x