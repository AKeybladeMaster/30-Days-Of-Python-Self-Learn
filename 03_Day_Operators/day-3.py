# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)

# Division in python gives floating number
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)

# gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Modulus: ', 3 % 2)                           # Gives the remainder
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison
# True - because the data values are the same
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False


# Exercises - Day 3

age = 25
height = 175.0
complex_num = 4 + 3j

# Input from user and calculating the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base * height
print('Area of triangle with base', base, 'and height', height, 'is:', area_of_triangle, "\n")

# Input from user and calculating the perimeter of a triangle
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print('Perimeter of triangle with sides', side_a, ',', side_b, 'and', side_c, 'is:', perimeter_of_triangle, "\n")

# Input from user and calculating the area and perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('Area of rectangle with length', length, 'and width', width, 'is:', area_of_rectangle)
print('Perimeter of rectangle with length', length, 'and width', width, 'is:', perimeter_of_rectangle, "\n")

# Input from user and calculating the area and circumference of a circle
radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
circumference_of_circle = 2 * 3.14 * radius
print('Area of circle with radius', radius, 'is:', area_of_circle)
print('Circumference of circle with radius', radius, 'is:', circumference_of_circle, "\n")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# For the equation y = 2x - 2, the slope (m) is 2 and the y-intercept (b) is -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print('Slope of the line is:', slope)
print('Y-intercept of the line is:', y_intercept)
print('X-intercept of the line is:', x_intercept, "\n")

# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Slope between the points is:', slope)
print('Euclidean distance between the points is:', euclidean_distance, "\n")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
# Response: The equation y = x^2 + 6x + 9 can be factored as y = (x + 3)^2. Therefore, y will be 0 when x = -3
# Result: x = -3

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
python_length = len('python')
dragon_length = len('dragon')
print('Length of python:', python_length)
print('Length of dragon:', dragon_length)
print('Is the length of python equal to the length of dragon?', python_length == dragon_length, "\n")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Is 'on' found in 'python' AND 'dragon'?", ('on' in 'python' and 'on' in 'dragon'), "\n")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
sentence = "I hope this course is not full of jargon."
print("Is 'jargon' found in the sentence?", 'jargon' in sentence, "\n")

# There is no 'on' in both dragon and python
print("There is NO 'on' in both 'dragon' and 'python':", not ('on' in 'dragon' and 'on' in 'python'), "\n")

# Find the length of the text python and convert the value to float and convert it to string
print('Length of "python" converted to float then string: ', str(float(len('python'))), "\n")

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
print("Is the number 10 even?", number % 2 == 0, "\n")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print("Is the floor division of 7 by 3 equal to the int converted value of 2.7?", 7 // 3 == int(2.7), "\n")

# Check if type of '10' is equal to type of 10
print('Is type of "10" equal to type of 10? ', type('10') == type(10), "\n")

# Check if int('9.8') is equal to 10
print('Is int(9.8) equal to 10? ', int(9.8) == 10, "\n")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
worked_hours = float(input("Enter the worked hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
print('Your weekly earning is ', worked_hours * rate_per_hour, "\n")

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = float(input("Enter number of years you have lived: "))
seconds = years_lived * 365 * 24 * 60 * 60
print("The person lived for", seconds, "seconds\n")

# Write a Python script that displays the following table 
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1,6):
    print(i, 1, i, i**2, i**3)