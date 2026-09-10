# Exercises - Day 22

import json
from html.parser import HTMLParser
from pathlib import Path

import requests


class PageParser(HTMLParser):
    """Collect readable page content and every HTML table without extra packages."""
    def __init__(self):
        super().__init__()
        self.title = ''
        self.headings = []
        self.paragraphs = []
        self.tables = []
        self._text_tag = None
        self._text = []
        self._table = None
        self._row = None
        self._cell = None

    def handle_starttag(self, tag, attrs):
        if tag in ('title', 'h1', 'h2', 'h3', 'p'):
            self._text_tag, self._text = tag, []
        elif tag == 'table':
            self._table = []
        elif tag == 'tr' and self._table is not None:
            self._row = []
        elif tag in ('th', 'td') and self._row is not None:
            self._cell = []

    def handle_data(self, data):
        if self._text_tag:
            self._text.append(data)
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag):
        if tag == self._text_tag:
            text = ' '.join(''.join(self._text).split())
            if tag == 'title':
                self.title = text
            elif tag.startswith('h') and text:
                self.headings.append(text)
            elif tag == 'p' and text:
                self.paragraphs.append(text)
            self._text_tag = None
        elif tag in ('th', 'td') and self._cell is not None:
            self._row.append(' '.join(''.join(self._cell).split()))
            self._cell = None
        elif tag == 'tr' and self._row is not None:
            if self._row:
                self._table.append(self._row)
            self._row = None
        elif tag == 'table' and self._table is not None:
            if self._table:
                self.tables.append(self._table)
            self._table = None


def fetch_page(url):
    response = requests.get(url, timeout=30, headers={'User-Agent': '30-Days-Of-Python learning project'})
    response.raise_for_status()
    parser = PageParser()
    parser.feed(response.text)
    return parser


def save_json(data, filename):
    path = Path(__file__).resolve().parent / filename
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return path


# 1. Scrape the Boston University facts and statistics website and store its data as JSON.
def scrape_bu_facts(url='https://www.bu.edu/president/boston-university-facts-stats/'):
    page = fetch_page(url)
    data = {'url': url, 'title': page.title, 'headings': page.headings, 'paragraphs': page.paragraphs, 'tables': page.tables}
    return save_json(data, 'bu_facts_and_stats.json')


# 2. Extract the UCI Machine Learning Repository tables and store them as JSON.
def scrape_uci_tables(url='https://archive.ics.uci.edu/ml/datasets.php'):
    page = fetch_page(url)
    return save_json({'url': url, 'tables': page.tables}, 'uci_datasets.json')


# 3. Scrape the United States presidents table and store the largest table as JSON.
def scrape_presidents_table(url='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'):
    page = fetch_page(url)
    presidents_table = max(page.tables, key=len, default=[])
    return save_json({'url': url, 'presidents': presidents_table}, 'us_presidents.json')


# Run every scraping assignment and print the saved JSON file path.
def run_assignment(name, scraper):
    try:
        print(f'{name} saved to ->', scraper())
    except requests.RequestException as error:
        print(f'{name} could not be downloaded ->', error)


run_assignment('Boston University facts and statistics', scrape_bu_facts)
run_assignment('UCI dataset tables', scrape_uci_tables)
run_assignment('United States presidents table', scrape_presidents_table)
