import requests
from src.parser import parse_vacancy

class HH:
    """
    Класс для работы с API HeadHunter.

    Attributes:
        BASE_URL (str): Базовый URL API.
        area_id (int): Идентификатор региона.
        vacancies (List[Vacancy]): Список вакансий.
    """
    BASE_URL = "https://api.hh.ru"

    def __init__(self, area_id):
        self.area_id = area_id
        self.vacancies = []

    def load_vacancies(self, search_query):
        """
        Загружает вакансии с API по заданному запросу.

        Args:
            search_query (str): Поисковый запрос.
        """
        page = 0
        per_page = 100  # Количество вакансий на странице
        total_pages = float('inf')

        while page < total_pages:
            response = requests.get(
                f"{self.BASE_URL}/vacancies",
                params={"area": self.area_id, "text": search_query, "page": page, "per_page": per_page}
            )
            data = response.json()
            self.vacancies.extend([parse_vacancy(item) for item in data.get('items', [])])

            if 'pages' in data:
                total_pages = data['pages']

            page += 1

    def get_vacancies(self):
        """
        Возвращает список загруженных вакансий.

        Returns:
            List[Vacancy]: Список вакансий.
        """
        return self.vacancies