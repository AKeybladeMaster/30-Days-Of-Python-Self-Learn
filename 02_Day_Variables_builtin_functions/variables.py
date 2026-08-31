
# Variables in Python: Level 1

first_name = 'Beasty'
last_name = 'Developer'
country = 'Italy'
city = 'Milan'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python', 'Java', 'MongoDB', 'Spring']
person_info = {
    'firstname': 'Beasty',
    'lastname': 'Developer',
    'country': 'Italy',
    'city': 'Milan'
}
is_true = True
is_light_on = False

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Beasty', 'Developer', 'Italy', 25, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Exercise: Level 2

print('Type of first name: ', type(first_name))
print('Type of last name: ', type(last_name))
print('Type of country: ', type(country))
print('Type of age: ', type(age))
print('Type of is_married: ', type(is_married))

print('Length of first name: ', len(first_name))
print('Length of last name: ', len(last_name))

num_one, num_two = 5, 4
sum = num_one + num_two
subtraction = num_two - num_one
multiplication = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
floor = num_one // num_two

# Print all the results

print('Sum: ', sum)
print('Subtraction: ', subtraction)
print('Multiplication: ', multiplication)
print('Division: ', division)
print('Remainder: ', remainder)
print('Floor: ', floor)

circle_radius = 30
area_of_circle = 3.14 * circle_radius ** 2
circum_of_circle = 2 * 3.14 * circle_radius

# Print all the results

print('Area of circle: ', area_of_circle)
print('Circumference of circle: ', circum_of_circle)

# Take radius as user input and calculate the area

circle_radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * circle_radius ** 2
print('Area of circle with radius', circle_radius, 'is:', area_of_circle)

# Use built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(help('keywords'))