import time
from bs4 import BeautifulSoup
import requests

HEADERS = (
    {'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

def web_scraper():
    """
    web_scraper
    :return:
    """
    url = "https://www.johnlewis.com/2020-apple-ipad-air-10-9-inch-a14-bionic-processor-ios-wi-fi-64gb/sky-blue/p5150321"
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="lxml")
    print(soup)

    title = soup.find('title').get_text().strip()
    price = soup.find('p', class_='price price--large')
    price = float(price.get_text().replace('£', '').strip()) if price else None
    print(f"{title}: £{price}")


if __name__ == "__main__":
    start_time = time.time()

    web_scraper()

    end_time = time.time()
    runtime = (end_time - start_time) / 60
    print(f"Runtime: {runtime:.2f} mins")
