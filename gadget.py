import requests
from bs4 import BeautifulSoup as BS
import csv



def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_last(soup):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    p = soup.find('ul', class_='pagination__list')
    page = p.find_all('li')[-2]
    return page.text


def get_data(soup):
    products = soup.find_all('div', class_='hit__slide')
    for pro in products:
        try:
            image = pro.find('img').get("src")
            image = 'https://www.gadget.kg' + image
        except:
            image = 'фото не указано'
        
        try:
            title = pro.find('h6', class_='hit__slide__title').find('a').get('title')
        except:
            title = 'Название не указно'

        try:
            price = pro.find('div', class_='hit__bot').find('span', class_='hit__slide__price').text.strip()
        except:
            price = 'Цена не указана'

        data = {
            "title": title,
            'price': price,
            'image': image
        }

        write_csv(data)


def write_csv(data):
    with open('phones.csv', 'a') as f:
        fieldnames = ['title', 'price','image']
        writer = csv.DictWriter(f, delimiter='/', fieldnames=fieldnames)
        writer.writerow(data)

def is_next(soup):
    p = soup.find('ul', class_='pagination__list')
    n = p.find("a", id="NextLink")
    return n

def main():
    BASE_URL = 'https://www.gadget.kg/catalog/telefony/planshety/'
    count = 1
    while True:
        url = f'{BASE_URL}?page={count}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last(soup)
        print(f'Страница {count}, Последняя страница {last_page}')
        get_data(soup)
        if not is_next(soup) or count > int(last_page):
            break
        count += 1

main()

# html = get_html('https://www.gadget.kg/catalog/telefony/planshety')
# soup = get_soup(html)
# get_data(soup)
