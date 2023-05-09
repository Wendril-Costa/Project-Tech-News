from datetime import datetime
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
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    cursor = get_collection().find({"timestamp": format_date})
    return [(document["title"], document["url"]) for document in cursor]


# Requisito 9
def search_by_category(category):
    collection = get_collection()
    cursor = collection.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": True, "url": True, "_id": False},
    )
    return [(document["title"], document["url"]) for document in cursor]
