# Exercises - Day 11

from collections import Counter
from math import pi, sqrt
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from data.countries_data import countries

# === LEVEL 1 ===

# Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(a, b): return a + b

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle
def area_of_circle(radius): return pi * radius ** 2

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*numbers): return sum(numbers) if all(isinstance(n, (int, float)) for n in numbers) else 'Numbers only'

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def convert_celsius_to_fahrenheit(celsius): return celsius * 9 / 5 + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
def check_season(month): return next((s for s, m in {'Autumn': (9,10,11), 'Winter': (12,1,2), 'Spring': (3,4,5), 'Summer': (6,7,8)}.items() if month in m), None)

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2): return (y2 - y1) / (x2 - x1)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
def solve_quadratic_eqn(a, b, c):
    d = b ** 2 - 4 * a * c
    return None if d < 0 else ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list(items): [print(item) for item in items]

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(items): return list(reversed(items))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items): return [item.capitalize() for item in items]

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(items, item): return items + [item]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it
def remove_item(items, item): return [value for value in items if value != item]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range
def sum_of_numbers(number): return sum(range(number + 1))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range
def sum_of_odds(number): return sum(range(1, number + 1, 2))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range
def sum_of_even(number): return sum(range(0, number + 1, 2))

# === LEVEL 2 ===

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number
def evens_and_odds(number): return {'odds': len(range(1, number + 1, 2)), 'evens': len(range(0, number + 1, 2))}

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number): return 1 if number < 2 else number * factorial(number - 1)

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value): return not bool(value)

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)
def calculate_mean(values): return sum(values) / len(values)

def calculate_median(values):
    values = sorted(values); middle = len(values) // 2
    return values[middle] if len(values) % 2 else (values[middle - 1] + values[middle]) / 2

def calculate_mode(values): return Counter(values).most_common(1)[0][0]

def calculate_range(values): return max(values) - min(values)

def calculate_variance(values): return sum((value - calculate_mean(values)) ** 2 for value in values) / len(values)

def calculate_std(values): return sqrt(calculate_variance(values))

# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name
def greet(name='Guest'): print(f'Hello, {name}!')

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values
def show_args(**kwargs): print(', '.join(f'{key}: {value}' for key, value in kwargs.items()))

# === LEVEL 3 ===

# Write a function called is_prime, which checks if a number is prime
def is_prime(number): return number > 1 and all(number % divisor for divisor in range(2, int(sqrt(number)) + 1))

# Write a functions which checks if all items are unique in the list
def all_unique(items): return len(items) == len(set(items))

# Write a function which checks if all the items of the list are of the same data type
def same_type(items): return len({type(item) for item in items}) <= 1

# Write a function which check if provided variable is a valid python variable
def valid_variable(name): return name.isidentifier()

# Go to the data folder and access the countries-data.py file:
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order
def most_spoken_languages(countries, limit=10): return Counter(language for c in countries for language in c['languages']).most_common(limit)
def most_populated_countries(countries, limit=10): return sorted(countries, key=lambda c: c['population'], reverse=True)[:limit]


if __name__ == '__main__':
    numbers = [1, 2, 2, 3, 4]
    words = ['python', 'hello', 'world']

    print('add_two_numbers:', add_two_numbers(2, 3))
    print('area_of_circle:', area_of_circle(5))
    print('add_all_nums:', add_all_nums(1, 2, 3.5))
    print('convert_celsius_to_fahrenheit:', convert_celsius_to_fahrenheit(25))
    print('check_season:', check_season(9))
    print('calculate_slope:', calculate_slope(1, 2, 3, 6))
    print('solve_quadratic_eqn:', solve_quadratic_eqn(1, -3, 2))
    print('print_list:')
    print_list(words)
    print('reverse_list:', reverse_list(words))
    print('capitalize_list_items:', capitalize_list_items(words))
    print('add_item:', add_item(words, 'code'))
    print('remove_item:', remove_item(numbers, 2))
    print('sum_of_numbers:', sum_of_numbers(10))
    print('sum_of_odds:', sum_of_odds(10))
    print('sum_of_even:', sum_of_even(10))
    print('evens_and_odds:', evens_and_odds(10))
    print('factorial:', factorial(5))
    print('is_empty:', is_empty([]))
    print('calculate_mean:', calculate_mean(numbers))
    print('calculate_median:', calculate_median(numbers))
    print('calculate_mode:', calculate_mode(numbers))
    print('calculate_range:', calculate_range(numbers))
    print('calculate_variance:', calculate_variance(numbers))
    print('calculate_std:', calculate_std(numbers))
    print('greet:')
    greet('Ada')
    print('show_args:')
    show_args(language='Python', level=11)
    print('is_prime:', is_prime(29))
    print('all_unique:', all_unique(words))
    print('same_type:', same_type(words))
    print('valid_variable:', valid_variable('valid_name'))
    print('most_spoken_languages:', most_spoken_languages(countries, 10))
    print('most_populated_countries:', [(country['name'], country['population']) for country in most_populated_countries(countries, 10)])
