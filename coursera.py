
import requests
import unicodedata
import json
from bs4 import BeautifulSoup

# https://www.coursera.org/browse/data-science/data-analysis?languages=en&page=1
json_data = {}
def spider(max_page):
    page = 1
    number = 0
    arr = []
    while page <= max_page:
        url = "https://www.coursera.org/browse/data-science/data-analysis?languages=en&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for found in soup.findAll('h2', {'class' : 'color-primary-text headline-1-text flex-1'}):
            text = found.string
            text = text.strip()
            if not text:
                continue
            print(text)
            arr.append(text)
        page += 1 
    json_data['all'] =  arr

spider(8)
print(json_data)
with open('coursera.json', 'w') as outfile:
    json.dump(json_data, outfile)