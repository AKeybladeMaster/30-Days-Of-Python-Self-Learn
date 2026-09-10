# Exercises - Day 19

import csv
import json
import re
import runpy
from collections import Counter
from pathlib import Path

# === LEVEL 1 ===

# 1. Write a function which counts the number of lines and words in a text.
#    Use it with obama_speech.txt, michelle_obama_speech.txt, donald_speech.txt, and melina_trump_speech.txt.
def count_lines_and_words(filename):
    text = Path(filename).read_text(encoding='utf-8')
    return {'lines': len(text.splitlines()), 'words': len(text.split())}

# Count lines and words in every speech file from the data folder.
DATA_FOLDER = Path(__file__).resolve().parents[1] / 'data'
for speech in ('obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt'):
    print(f'{speech} ->', count_lines_and_words(DATA_FOLDER / speech))

# 2. Read countries_data.json and create a function that finds the ten most spoken languages.
def load_countries(filename):
    """Load either a JSON countries file or the provided countries_data.py file."""
    path = Path(filename)
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return runpy.run_path(path)['countries']

def most_spoken_languages(filename, number=10):
    countries = load_countries(filename)
    languages = Counter(language for country in countries for language in country['languages'])
    return [(count, language) for language, count in languages.most_common(number)]

# 3. Read countries_data.json and create a list of the ten most populated countries.
def most_populated_countries(filename, number=10):
    countries = load_countries(filename)
    countries = sorted(countries, key=lambda country: country['population'], reverse=True)
    return [{'country': country['name'], 'population': country['population']} for country in countries[:number]]

# Run the language and population assignments with countries_data.json.
COUNTRIES_DATA = DATA_FOLDER / 'countries_data.json'
print(most_spoken_languages(COUNTRIES_DATA, 10))
print(most_populated_countries(COUNTRIES_DATA, 10))

# === LEVEL 2 ===

# 1. Extract all incoming email addresses as a list from email_exchange_big.txt.
def extract_emails(filename):
    text = Path(filename).read_text(encoding='utf-8')
    return re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', text)

# Extract the incoming email addresses from the supplied email exchange file.
incoming_emails = extract_emails(DATA_FOLDER / 'email_exchanges_big.txt')
print('Incoming email addresses found ->', len(incoming_emails))

# 2. Find the most common words in a string or file and return descending tuples.
def read_text(source):
    path = Path(source)
    return path.read_text(encoding='utf-8') if path.is_file() else str(source)

def find_most_common_words(source, number=10):
    words = re.findall(r"[A-Za-z']+", read_text(source).lower())
    return [(count, word) for word, count in Counter(words).most_common(number)]


# 3. Find the ten most frequent words in each of the four speeches.
def find_most_frequent_words(source, number=10):
    return find_most_common_words(source, number)

# Find the ten most frequent words in each supplied speech.
for speech in ('obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt'):
    print(f'Most frequent words in {speech} ->', find_most_frequent_words(DATA_FOLDER / speech, 10))

# 4. Check the similarity between two texts after cleaning and removing support words.
def clean_text(text):
    return re.sub(r'[^a-z ]', '', text.lower())

def remove_support_words(text, support_words):
    return [word for word in clean_text(text).split() if word not in support_words]

def check_text_similarity(first, second, support_words=()):
    first_words = set(remove_support_words(read_text(first), support_words))
    second_words = set(remove_support_words(read_text(second), support_words))
    return len(first_words & second_words) / len(first_words | second_words) if first_words | second_words else 0

# Compare Michelle Obama's and Melina Trump's speeches without support words.
support_words = runpy.run_path(DATA_FOLDER / 'stop_words.py')['stop_words']
similarity = check_text_similarity(DATA_FOLDER / 'michelle_obama_speech.txt', DATA_FOLDER / 'melina_trump_speech.txt', support_words)
print('Speech similarity ->', round(similarity, 3))

# 5. Find the ten most repeated words in romeo_and_juliet.txt.
print('Most repeated words in Romeo and Juliet ->', find_most_frequent_words(DATA_FOLDER / 'romeo_and_juliet.txt', 10))

# 6. Read hacker_news.csv and count Python, JavaScript, and Java-but-not-JavaScript lines.
def hacker_news_counts(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        rows = list(csv.reader(file))

    lines = [' '.join(row).lower() for row in rows]
    return {
        'python': sum('python' in line for line in lines),
        'javascript': sum('javascript' in line for line in lines),
        'java_not_javascript': sum('java' in line and 'javascript' not in line for line in lines)
    }

# Count Hacker News lines containing Python, JavaScript, and Java without JavaScript.
print('Hacker News counts ->', hacker_news_counts(DATA_FOLDER / 'hacker_news.csv'))
