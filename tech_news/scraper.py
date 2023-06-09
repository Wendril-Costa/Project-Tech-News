import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    return sel.css("header h2 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    next_page = sel.css("a.next::attr(href)").get()
    return next_page if next_page else None


# Requisito 4
def scrape_news(html_content):
    sel = Selector(html_content)
    data = {}
    data["url"] = sel.css('link[rel="canonical"]::attr(href)').get()
    data["title"] = sel.css("h1.entry-title::text").get().strip()
    data["timestamp"] = sel.css("li.meta-date::text").get().strip()
    data["writer"] = (
        sel.css("li.meta-author span.author a::text").get().strip()
    )
    data["reading_time"] = int(
        sel.css("li.meta-reading-time::text").get().split()[0]
    )
    data["summary"] = "".join(
        sel.css(".entry-content > p:first-of-type ::text").getall()
    ).strip()
    data["category"] = sel.css(".category-style .label::text").get().strip()
    return data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        for link in scrape_updates(fetch(url)):
            news.append(scrape_news(fetch(link)))
            if len(news) == amount:
                break
        url = scrape_next_page_link(fetch(url))
    create_news(news)
    return news[:amount]
