import json
import pytest
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

@pytest.fixture
def vacancy():
    """
    Фикстура для создания экземпляра Vacancy.

    Returns:
        Vacancy: Экземпляр класса Vacancy.
    """
    return Vacancy("1", "Test", {"from": 1000, "to": 2000, "currency": "RUR", "gross": False}, "City", "Street", "Description")

@pytest.fixture
def json_saver(tmp_path):
    """
    Фикстура для создания экземпляра JSONSaver.

    Args:
        tmp_path (Path): Временный путь для сохранения JSON файла.

    Returns:
        JSONSaver: Экземпляр класса JSONSaver.
    """
    file_path = tmp_path / "test_vacancies.json"
    return JSONSaver(file_path)

def test_save_to_json(vacancy, json_saver):
    """
    Тестирует метод save класса JSONSaver.

    Args:
        vacancy (Vacancy): Экземпляр класса Vacancy.
        json_saver (JSONSaver): Экземпляр класса JSONSaver.
    """
    json_saver.save([vacancy])
    with open(json_saver.file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert data == [vacancy.to_dict()]

def test_load_from_json(vacancy, json_saver):
    """
    Тестирует метод load класса JSONSaver.

    Args:
        vacancy (Vacancy): Экземпляр класса Vacancy.
        json_saver (JSONSaver): Экземпляр класса JSONSaver.
    """
    with open(json_saver.file_path, "w", encoding="utf-8") as file:
        json.dump([vacancy.to_dict()], file)
    loaded_vacancies = json_saver.load()
    assert loaded_vacancies == [vacancy.to_dict()]
