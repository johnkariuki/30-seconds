import requests
from bs4 import BeautifulSoup
import unicodedata
import json

brands = {
    'brands': []
}


def spider():
    url = 'http://interbrand.com/best-brands/best-global-brands/2016/ranking/'
    connect = requests.get(url)
    plain_text = connect.text
    soup_object = BeautifulSoup(plain_text, "html.parser")
    for links in soup_object.findAll('div', {'class': 'brand-name'}):
        normalised_brands = unicodedata.normalize('NFKD', links.string).encode('ascii', 'ignore')
        brands['brands'].append((normalised_brands).replace('\n', '').replace(' ', ''))
    return brands


def write_to_file():
    with open('brands.json', 'w') as file:
        json.dump(str(spider()), file)
        print('Written to brands file.')

write_to_file()
