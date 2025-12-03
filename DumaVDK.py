from urllib.parse import urljoin
from pathlib import Path
import csv
import re
import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_DIR = Path(__file__).parent
MAIN_DOC_URL = 'https://www.dumavlad.ru/'
CSV_FILE = BASE_DIR / 'dumavlad_news.csv'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    soup = BeautifulSoup(response.text, features='lxml')
    news_div = soup.find('div', attrs={'id': 'workarea'})
    news_links = news_div.find_all('a', href=lambda x: x and x.startswith('/news/2'))
    links = []
    for link in news_links:
        links.append(urljoin(MAIN_DOC_URL, link['href']))
    results = []
    for new in tqdm(links):
        response = session.get(new)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')
        new_text = soup.find('h2', attrs={'class': 'content-block__title'})
        date = soup.find('span')
        results.append((new_text.text[5:], date.text, new))
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Заголовок', 'Дата', 'URL'])
        writer.writerows(results)
    print(f"Сохранено {len(results)} новостей в {CSV_FILE}")
    print(f"Первые 3 записи: {results[:3]}")