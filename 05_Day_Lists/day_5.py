import math

empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0

# list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing itmes
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
fruits.append('lime')
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
fruits.insert(3, 'lime')
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# Exercises - Day 5

# === LEVEL 1 ===

# Declare an empty list
empty_list = list()

# Declare a list with more than 5 items
five_items_list = ['One', 'Two', 'Three', 'Four', 'Five']

# Find the length of your list
print('Length of the five items list: {}'.format(len(five_items_list)))

# Get the first item, the middle item and the last item of the list
print('First item -> {}, middle item -> {}, last item -> {}'.format(five_items_list[0], five_items_list[len(five_items_list) // 2], five_items_list[len(five_items_list) - 1]))

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Beasty', '25', '100', 'Taken', 'Milan, Italy']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print('IT companies list -> ', it_companies)

# Print the number of companies in the list
print('Number of companies in the list -> ', len(it_companies))

# Print the first, middle and last company
print('First company -> {}, middle company -> {}, last company -> {}'.format(it_companies[0], it_companies[len(it_companies) // 2], it_companies[len(it_companies) - 1]))

# Print the list after modifying one of the companies
print('Modified companies list -> ', it_companies.remove('Oracle'))

# Add an IT company to it_companies
it_companies.append('Accenture')

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Robinhood')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# Join the it_companies with a string '#;  '
print('Joined IT companies with #;  -> ', "#;  ".join(it_companies))

# Check if a certain company exists in the it_companies list.
print('Does Innodata exist in the list? -> {} occurrence(s) found'.format(it_companies.count('Innodata')))

# Sort the list using sort() method
print('List of IT companies sorted -> ', it_companies.sort())

# Reverse the list in descending order using reverse() method
print('List of IT companies sorted (reverse) -> ', it_companies.reverse())

# Slice out the first 3 companies from the list
print('First 3 companies sliced out -> ', it_companies[3:])

# Slice out the last 3 companies from the list
print('Last 3 companies sliced out -> ', it_companies[-3:])

# Slice out the middle IT company or companies from the list
print('Middle IT company(ies) sliced out -> ', it_companies[math.floor(len(it_companies) / 2):math.ceil(len(it_companies) / 2)])

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
it_companies.pop(math.floor(len(it_companies) // 2))

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
redux_index = full_stack.index('Redux') + 1
full_stack[redux_index:redux_index] = ['Python', 'SQL']
print('Full stack variable final print -> ', full_stack)


# === LEVEL 2 ===

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[len(ages) - 1]

# Add the min age and the max age again to the list
ages[len(ages) + 1 : len(ages) + 1] = [min_age, max_age]

# Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 != 0:
    median_age = (ages[math.floor(len(ages) / 2)] + ages[math.ceil(len(ages) / 2)]) // 2
else:
    median_age = (ages[len(ages) // 2])

# Find the average age (sum of all items divided by their number )
age_sum = 0

for age in ages:
    age_sum += age

average = age_sum // len(ages)

# Find the range of the ages (max minus min)
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_age - average)
max_average = abs(max_age - average)

# SKIPPING THE COUNTRIES EXERCISES