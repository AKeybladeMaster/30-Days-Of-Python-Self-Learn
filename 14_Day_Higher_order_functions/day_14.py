# Exercises - Day 14

from functools import reduce
from collections import Counter
from pathlib import Path
import sys

# Make the project root available when this file is run directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
from data.countries import countries as all_countries
from data.countries_data import countries as countries_data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Beasty', 'Lidiya', 'Ermias', 'Abraham']
numbers = list(range(1, 11))

# === LEVEL 1 ===

# map transforms items, filter keeps matching items, and reduce combines items.
# A higher-order function receives/returns functions; a closure remembers scope; a decorator wraps a function.

# Use for loop to print each country in the countries list
# Use for to print each name in the names list
# Use for to print each number in the numbers list
for items in (countries, names, numbers):
    for item in items: print(item)

# === LEVEL 2 ===

# Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(str.upper, countries)))

# Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda number: number ** 2, numbers)))

# Use map to change each name to uppercase in the names list
print(list(map(str.upper, names)))

# Use filter to filter out countries containing 'land'
print(list(filter(lambda country: 'land' in country.lower(), countries)))

# Use filter to filter out countries having exactly six characters
print(list(filter(lambda country: len(country) == 6, countries)))

# Use filter to filter out countries containing six letters and more in the country list
print(list(filter(lambda country: len(country) >= 6, countries)))

# Use filter to filter out countries starting with an 'E'
print(list(filter(lambda country: country.startswith('E'), countries)))

# Chain filter and map to uppercase countries with six or more letters
print(list(map(str.upper, filter(lambda country: len(country) >= 6, countries))))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(items): return [item for item in items if isinstance(item, str)]
print(get_string_lists(['Python', 30, 'Days', True]))

# Use reduce to sum all the numbers in the numbers list
print(reduce(lambda total, number: total + number, numbers))

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print(reduce(lambda left, right: f'{left}, {right}', countries[:-1]) + f', and {countries[-1]} are north European countries')

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan'))
def categorize_countries(items, pattern='land'): return [item for item in items if pattern.lower() in item.lower()]
print(categorize_countries(all_countries, 'land'))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter
def starting_letter_count(items): return dict(Counter(item[0] for item in items))
print(starting_letter_count(all_countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder
def get_first_ten_countries(items): return items[:10]
print(get_first_ten_countries(all_countries))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list
def get_last_ten_countries(items): return items[-10:]
print(get_last_ten_countries(all_countries))

# === LEVEL 3 ===

# Use the countries_data.py to:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location
# Sort out the ten most populated countries
def sort_countries(data, field): return sorted(data, key=lambda country: country.get(field) or '')

countries_by_name = sort_countries(countries_data, 'name')
countries_by_capital = sort_countries(countries_data, 'capital')
countries_by_population = sorted(countries_data, key=lambda country: country.get('population', 0), reverse=True)

print('Countries sorted by name ->', [country['name'] for country in countries_by_name[:10]])
print('Countries sorted by capital ->', [country['name'] for country in countries_by_capital[:10]])
print('Countries sorted by population ->', [country['name'] for country in countries_by_population[:10]])

language_counts = Counter(language for country in countries_data for language in country['languages'])
print('Ten most spoken languages ->', language_counts.most_common(10))
print('Ten most populated countries ->', [(country['name'], country['population']) for country in countries_by_population[:10]])
