# src/parser.py

from src.vacancy import Vacancy

def parse_vacancy(api_response):
    """
    Парсит ответ API и создает объект Vacancy.

    Args:
        api_response (dict): Ответ API в формате словаря.

    Returns:
        Vacancy: Экземпляр класса Vacancy.
    """
    title = api_response.get('name', '')
    url = api_response.get('alternate_url', '')
    salary_info = api_response.get('salary', {})
    if salary_info is not None:
        salary = {
            'from': salary_info.get('from', 0),
            'to': salary_info.get('to', 0),
            'currency': salary_info.get('currency', ''),
            'gross': salary_info.get('gross', False)
        }
    else:
        salary = {
            'from': 0,
            'to': 0,
            'currency': '',
            'gross': False
        }

    snippet_info = api_response.get('snippet', {})
    requirement = snippet_info.get('requirement', '')
    responsibility = snippet_info.get('responsibility', '')
    address_info = api_response.get('address', {})
    city = address_info.get('city', '') if address_info else ''
    street = address_info.get('street', '') if address_info else ''
    description = f"{requirement}\n{responsibility}"
    return Vacancy(url, title, salary, city, street, description)
