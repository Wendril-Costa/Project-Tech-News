from tech_news.database import get_collection


# Requisito 7
def search_by_title(title):
    collection = get_collection()
    cursor = collection.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": True, "url": True, "_id": False},
    )
    return [(document["title"], document["url"]) for document in cursor]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
