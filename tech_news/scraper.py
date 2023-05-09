import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return None
    return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(html_content)
    return [card.css('a::attr(href)').get() for card in sel.css('.post')[1:]]


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    next_page = sel.css('a.next::attr(href)').get()
    return next_page if next_page else None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
