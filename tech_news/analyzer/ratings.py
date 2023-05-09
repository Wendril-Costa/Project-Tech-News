from tech_news.database import get_collection


def top_5_categories():
    collection = get_collection()
    cursor = collection.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5}
    ])
    return [category["_id"] for category in cursor]
