# Exercises - Day 18

import re
from collections import Counter

# === LEVEL 1 ===

def most_frequent_words(text, count=None):
    words = re.findall(r"[A-Za-z]+", text)
    return [(total, word) for word, total in Counter(words).most_common(count)]

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
print(most_frequent_words(paragraph))

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles
points = list(map(int, re.findall(r'-?\d+', '-12, -4, -3, -1, 0, 4 and 8')))
print(points, max(points) - min(points))

# === LEVEL 2 ===

def is_valid_variable(name): return bool(re.fullmatch(r'[A-Za-z_]\w*', name))
print(is_valid_variable('firstname'))
print(is_valid_variable('1first_name'))

# === LEVEL 3 ===

def clean_text(text): return re.sub(r'[^A-Za-z ]', '', text)

sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text, 3))
