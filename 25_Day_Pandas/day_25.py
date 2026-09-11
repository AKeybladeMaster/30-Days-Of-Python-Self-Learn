# Exercises - Day 25

import pandas as pd

def explore_hacker_news(filename='data/hacker_news.csv'):
    news = pd.read_csv(filename)
    titles = news['title'].fillna('')
    return {'first_five': news.head(), 'last_five': news.tail(), 'titles': titles,
            'shape': news.shape, 'python_titles': news[titles.str.contains('python', case=False)],
            'javascript_titles': news[titles.str.contains('javascript', case=False)],
            'summary': news.describe(include='all')}

results = explore_hacker_news()
print(results['shape'])
