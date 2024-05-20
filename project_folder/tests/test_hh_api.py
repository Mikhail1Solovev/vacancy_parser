# tests/test_hh_api.py

import pytest
from src.hh_api import HH
from src.vacancy import Vacancy
import requests_mock


@pytest.fixture
def hh_instance():
    """
    Фикстура для создания экземпляра HH.

    Returns:
        HH: Экземпляр класса HH.
    """
    return HH(1)


def test_load_vacancies(requests_mock):
    """
    Тестирует метод load_vacancies.

    Args:
        requests_mock (Mocker): Мок для requests.
    """
    api_response = {
        "items": [
            {
                "name": "JavaScript Developer",
                "alternate_url": "https://hh.ru/vacancy/12345",
                "salary": {"from": 1000, "to": 2000, "currency": "RUR", "gross": True},
                "snippet": {"requirement": "Strong JavaScript skills", "responsibility": "Developing web applications"},
                "address": {"city": "Moscow", "street": "Tverskaya"}
            }
        ],
        "pages": 1
    }
    requests_mock.get("https://api.hh.ru/vacancies", json=api_response)
    hh = HH(1)
    hh.load_vacancies("JavaScript")
    vacancies = hh.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].name == "JavaScript Developer"


def test_get_vacancies(hh_instance):
    """
    Тестирует метод get_vacancies.

    Args:
        hh_instance (HH): Экземпляр класса HH.
    """
    vacancy = Vacancy("1", "Test", {"from": 1000, "to": 2000, "currency": "RUR", "gross": False}, "City", "Street",
                      "Description")
    hh_instance.vacancies.append(vacancy)
    vacancies = hh_instance.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].id == "1"
