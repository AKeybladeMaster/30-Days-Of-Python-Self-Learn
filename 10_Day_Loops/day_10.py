# Exercises - Day 10

from pathlib import Path
import sys
import json

# Make the project root available when this file is run directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
from data.countries import countries

# countries_data.py contains JSON data, so load it from the file.
with open(PROJECT_ROOT / 'data' / 'countries_data.py', encoding='utf-8') as file:
    countries_data = json.load(file)

# === LEVEL 1 ===

# Count up and down with for and while loops
for number in range(11): print(number, end=' ')
print()

number = 10
while number >= 0:
    print(number, end=' ')
    number -= 1
print()

# Patterns and basic loops
for number in range(1, 8): 
    print('#' * number)

for _ in range(8): 
    print('# ' * 8)
for number in range(11): 
    print(f'{number} x {number} = {number ** 2}')

for technology in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']: 
    print(technology)

print(list(range(0, 101, 2)))

print(list(range(1, 101, 2)))

# === LEVEL 2 ===

# Sums using for loops
total, even_total, odd_total = 0, 0, 0
for number in range(101):
    total += number
    if number % 2 == 0:
        even_total += number
    else:
        odd_total += number

print('The sum of all numbers is', total)
print('The sum of all evens is', even_total, 'and the sum of all odds is', odd_total)

# === LEVEL 3 ===

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

# Import and loop through the countries data to find countries containing 'land'
from collections import Counter

def countries_with_land(countries): return [country for country in countries if 'land' in country.lower()]

countries_containing_land = countries_with_land(countries)
print('Countries containing land ->', countries_containing_land)

# Go to the data folder and use the countries_data.py file
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
def language_and_population_top_ten(countries_data):
    languages = Counter(language for country in countries_data for language in country.get('languages', []))
    populated = sorted(countries_data, key=lambda country: country.get('population', 0), reverse=True)
    return languages.most_common(10), populated[:10]

# Find the ten most spoken languages and the ten most populated countries.
most_spoken_languages, most_populated_countries = language_and_population_top_ten(countries_data)
print('Ten most spoken languages ->', most_spoken_languages)
print('Ten most populated countries ->', most_populated_countries)
