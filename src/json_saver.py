import json
from abc import ABC, abstractmethod
from typing import List
from src.vacancy import Vacancy


class AbstractJSONSaver(ABC):
    """
    Абстрактный класс для сохранения и загрузки данных в/из JSON файла.

    Attributes:
        file_path (str): Путь к JSON файлу.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def save(self, data: List[dict]) -> None:
        """
        Сохраняет список словарей в файл в формате JSON.

        Args:
            data (List[dict]): Список словарей для сохранения.
        """
        pass

    @abstractmethod
    def load(self) -> List[dict]:
        """
        Загружает список словарей из файла.

        Returns:
            List[dict]: Загруженный список словарей.
        """
        pass


class JSONSaver(AbstractJSONSaver):
    """
    Класс для сохранения и загрузки объектов Vacancy в/из JSON файла.
    """

    def save(self, vacancies: List[Vacancy]) -> None:
        """
        Сохраняет список объектов Vacancy в файл в формате JSON.

        Args:
            vacancies (List[Vacancy]): Список объектов Vacancy для сохранения.
        """
        data = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self) -> List[dict]:
        """
        Загружает список словарей из файла.

        Returns:
            List[dict]: Список словарей, представляющих вакансии.
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)