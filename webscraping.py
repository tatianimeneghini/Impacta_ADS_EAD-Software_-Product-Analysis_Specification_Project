from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import math 

URL = 'https://www.kabum.com.br/celular-smartphone/smartphones/iphone/iphone-14?page_number=1&page_size=20&facet_filters=eyJBcm1hemVuYW1lbnRvIjpbIjI1NiBHQiJdfQ==&sort=most_searched'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"
}
website = requests.get(URL, headers)
soup = BeautifulSoup(website, 'html.parser')

print('Caso de aceite funcionando.')
print(soup.find_all("a", class_="productCard"))