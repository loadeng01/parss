import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

# def get_soup(html):
#     soup = BS(html, 'lxml')
#     return soup

# def get_data(soup):
#     catalog = soup.find('div', class_='row')
#     products = catalog.find_all('div', class_='product-thumb')
#     for pro in products:
#         name = pro.find('div', class_='caption').find('div', class_='name').text.strip()
#         price = pro.find('div', class_='caption').find('div', class_='price').text.strip()
#         img = pro.find('div', class_='image').find('a', class_='lazy').find('img', class_='img-responsive').get("data-src")
#         print(img)
#         print(name, price)
        
    

# html =  get_html('https://softech.kg/smart-chasy-')
# soup = get_soup(html)
# get_data(soup)

# print(requests.get('https://stackoverflow.com/questions'))

