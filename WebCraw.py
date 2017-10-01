import requests
import unicodedata
import json
from bs4 import BeautifulSoup

json_data = {}
def spider():
    url = "https://www.udacity.com/courses/all"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for found in soup.findAll('p', {'class' : 'form-control-static'}):
        link = found.find('a')
        text = link.string
        text = text.strip()
        if not text:
            continue
        href = "https://www.udacity.com" + link.get('href')
        print(text)
        json_data[text] =  spiderinside((href))

#<h3 class="h-slim">
def spiderinside(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    arr = []
    for found in soup.findAll('h3', {'class', 'h-slim'}):
        link = found.find('a')
        text = link.string
        text = text.strip()
        if not text:
            continue
        href = "https://www.udacity.com" + link.get('href')
        print('\t' + text)
        # print(href)
        arr.append(text)
    return arr 

spider()
print(json_data)
with open('udacity.json', 'w') as outfile:
    json.dump(json_data, outfile)






    