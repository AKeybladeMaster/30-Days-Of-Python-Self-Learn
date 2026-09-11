# Exercises - Day 26

import re
from collections import Counter

def analyse_text(text):
    words = re.findall(r"[A-Za-z']+", text.lower())
    sentences = [sentence for sentence in re.split(r'[.!?]+', text) if sentence.strip()]
    return {'characters': len(text), 'words': len(words), 'sentences': len(sentences),
            'most_common_words': Counter(words).most_common(10)}

print(analyse_text('Python makes text analysis quick. Python is readable!'))
