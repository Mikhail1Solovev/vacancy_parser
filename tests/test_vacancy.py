# tests/test_vacancy.py

import pytest
from src.vacancy import Vacancy

def test_vacancy_initialization():
    vacancy = Vacancy("1", "Test", {"from": 1000, "to": 2000, "currency": "RUR", "gross": False}, "City", "Street", "Description")
    assert vacancy.id == "1"
    assert vacancy.name == "Test"
    assert vacancy.salary == {"from": 1000, "to": 2000, "currency": "RUR", "gross": False}
    assert vacancy.city == "City"
    assert vacancy.street == "Street"
    assert vacancy.description == "Description"

def test_vacancy_to_dict():
    vacancy = Vacancy("1", "Test", {"from": 1000, "to": 2000, "currency": "RUR", "gross": False}, "City", "Street", "Description")
    expected_dict = {
        "id": "1",
        "name": "Test",
        "salary": {"from": 1000, "to": 2000, "currency": "RUR", "gross": False},
        "city": "City",
        "street": "Street",
        "description": "Description"
    }
    assert vacancy.to_dict() == expected_dict

# Добавьте дополнительные тесты для всех других методов и сценариев использования класса Vacancy
