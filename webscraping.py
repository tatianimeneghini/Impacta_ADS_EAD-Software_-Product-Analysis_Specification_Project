import math
from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.kabum.com.br/celular-smartphone/smartphones/iphone/iphone-14?page_number=1&page_size=100&facet_filters=eyJBcm1hemVuYW1lbnRvIjpbIjI1NiBHQiJdfQ==&sort=most_searched'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"
}
website = requests.get(url, headers=headers)
soup = BeautifulSoup(website.content, 'html.parser')

quantity_items = soup.find('div', id='listingCount').get_text().strip()
index = quantity_items.find(' ')
quantity = quantity_items[:index]
last_page = math.ceil(int(quantity)/50)

all_products = {'produto': [], 'valor': []}
products = soup.find_all('div', class_=re.compile('productCard'))

for i in range(0, last_page + 1):
    url_page = f'https://www.kabum.com.br/celular-smartphone/smartphones/iphone/iphone-14?page_number={i}&page_size=100&facet_filters=eyJBcm1hemVuYW1lbnRvIjpbIjI1NiBHQiJdfQ==&sort=most_searched'
    website = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(website.content, 'html.parser')
    products = soup.find_all('div', class_=re.compile('productCard'))
    for product in products:
        preco = product.find('span', class_=re.compile('priceCard')).get_text().strip()
        produto = product.find('span', class_=re.compile('nameCard')).get_text().strip()
            
        all_products['produto'].append(produto)
        all_products['valor'].append(preco)
    
print(all_products)