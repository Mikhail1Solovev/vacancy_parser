# tests/test_parser.py

from src.parser import parse_vacancy

def test_parse_vacancy():
    """
    Тестирует функцию parse_vacancy.
    """
    api_response = {
        "name": "JavaScript Developer",
        "alternate_url": "https://hh.ru/vacancy/12345",
        "salary": {"from": 1000, "to": 2000, "currency": "RUR", "gross": True},
        "snippet": {"requirement": "Strong JavaScript skills", "responsibility": "Developing web applications"},
        "address": {"city": "Moscow", "street": "Tverskaya"}
    }
    vacancy = parse_vacancy(api_response)
    assert vacancy.name == "JavaScript Developer"
    assert vacancy.salary == {"from": 1000, "to": 2000, "currency": "RUR", "gross": True}
    assert vacancy.city == "Moscow"
    assert vacancy.street == "Tverskaya"
    assert vacancy.description == "Strong JavaScript skills\nDeveloping web applications"
