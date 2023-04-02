from bs4 import BeautifulSoup
import requests

url = 'https://www.kabum.com.br/celular-smartphone/smartphones/iphone/iphone-14?page_number=1&page_size=100&facet_filters=eyJBcm1hemVuYW1lbnRvIjpbIjI1NiBHQiJdfQ==&sort=most_searched'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"
}
website = requests.get(url, headers=headers)
soup = BeautifulSoup(website.content, 'html.parser')

products = soup.find("div", id="listingCount").get_text().strip()
index_products = products.find(' ')
total_products = products[:index_products]
print('A quantidade total de produtos é: ' + total_products)

items = soup.select("div a.htpbqG", class_="productCard")
print('Os produtos retornados são: ')
print(items)

# Garantir que seja a mesma quantidade: <a class="