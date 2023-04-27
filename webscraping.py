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

items = soup.select("div a.tEYzR", class_="productCard")
prices = soup.select("span.hQOqhY", class_="priceCard")

print("Os valores dos produtos disponíveis são: ")
for price in prices:
    if (price != "R$ ---"):
        print(price.get_text())

# print("------------------------")
# print("Todos os produtos selecionados são: ")
for item in items:
    print(item.text)