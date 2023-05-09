import pytest
from unittest.mock import MagicMock
from tech_news.analyzer.reading_plan import ReadingPlanService


@pytest.fixture
def mock_news():
    return [
        {
            "url": "https://site.com/post1",
            "title": "Descoberta de nova espécie animal",
            "timestamp": "2023-05-03T17:45:01",
            "writer": "Charles Darwin",
            "reading_time": 1,
            "summary": "Uma descoberta que pode mudar",
            "category": "Biologia",
        },
        {
            "url": "https://site.com/post2",
            "title": "Descoberta científica revolucionária",
            "timestamp": "2023-05-01T12:34:56",
            "writer": "Albert Einstein",
            "reading_time": 15,
            "summary": "Uma descoberta incrível",
            "category": "Ciência",
        },
    ]


def test_reading_plan_group_news(mock_news):
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_news)
    resul = ReadingPlanService.group_news_for_available_time(10)

    assert len(resul["readable"]) == 1
    assert len(resul["unreadable"]) == 1
    assert resul["readable"][0]["unfilled_time"] == 9
