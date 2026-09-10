# Exercises - Day 20

import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from statistics import mean, median, stdev
from urllib.parse import urljoin

import requests

DATA_FOLDER = Path(__file__).resolve().parents[1] / 'data'

# 1. Read Romeo and Juliet and find its ten most frequent words.
def most_frequent_words(filename, number=10):
    text = Path(filename).read_text(encoding='utf-8').lower()
    return Counter(re.findall(r'[a-z]+', text)).most_common(number)

print('Romeo and Juliet: ', most_frequent_words(DATA_FOLDER / 'romeo_and_juliet.txt'))

# 2. Read the cats data and calculate statistics for weight and lifespan.
def number_range(value):
    numbers = [int(number) for number in re.findall(r'\d+', value)]
    return mean(numbers)

def summary(values):
    return {
        'min': min(values),
        'max': max(values),
        'mean': round(mean(values), 2),
        'median': median(values),
        'standard_deviation': round(stdev(values), 2)
    }

def cat_statistics(filename):
    breeds = json.loads(Path(filename).read_text(encoding='utf-8'))
    weights = [number_range(breed['weight']['metric']) for breed in breeds]
    lifespans = [number_range(breed['life_span']) for breed in breeds]
    country_and_breed = Counter((breed.get('origin', 'Unknown'), breed['name']) for breed in breeds)
    return {'weight': summary(weights), 'lifespan': summary(lifespans), 'country_and_breed': country_and_breed}

cats = cat_statistics(DATA_FOLDER / 'cats.json')
print('Cat weight statistics: ', cats['weight'])
print('Cat lifespan statistics: ', cats['lifespan'])
print('Cat country and breed frequency table: ', cats['country_and_breed'])

# 3. Read the countries data and find the largest countries, languages, and language total.
def countries_summary(filename, number=10):
    countries = json.loads(Path(filename).read_text(encoding='utf-8'))
    largest = sorted(countries, key=lambda country: country.get('area', 0), reverse=True)[:number]
    languages = Counter(
        language['name'] if isinstance(language, dict) else language
        for country in countries for language in country.get('languages', [])
    )
    return {
        'largest': [(country['name'], country.get('area', 0)) for country in largest],
        'most_spoken_languages': languages.most_common(number),
        'total_languages': sum(len(country.get('languages', [])) for country in countries)
    }

# countries_data_long.json includes geographical area, which is needed for largest countries.
country_results = countries_summary(DATA_FOLDER / 'countries_data_long.json')
print('Ten largest countries: ', country_results['largest'])
print('Ten most spoken languages: ', country_results['most_spoken_languages'])
print('Total languages: ', country_results['total_languages'])

# 4. Read the UCI datasets page and return its first ten dataset links.
class DatasetLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href and 'dataset' in href.lower():
                self.links.append(href)

def uci_dataset_links(url='https://archive.ics.uci.edu/ml/datasets.php', number=10):
    parser = DatasetLinkParser()
    parser.feed(requests.get(url, timeout=20).text)
    return [urljoin(url, link) for link in dict.fromkeys(parser.links)][:number]

try:
    print('UCI dataset links: ', uci_dataset_links())
except requests.RequestException as error:
    print('UCI dataset links could not be loaded: ', error)
