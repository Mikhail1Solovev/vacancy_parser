from src.hh_api import HH
from src.json_saver import JSONSaver
from pprint import pprint

def user_interaction():
    """
    Основная функция для взаимодействия с пользователем.
    """
    action = input(
        "1. Ввести поисковый запрос\n"
        "2. Получить топ N вакансий по зарплате\n"
        "3. Получить вакансии с ключевым словом в описании\n"
        "4. Выйти\n"
        "Выберите действие: "
    )

    hh_instance = HH(1)  # Введите ваш area_id
    json_saver = JSONSaver("data/vacancies.json")

    if action == "1":
        search_query = input("Введите поисковый запрос: ")
        hh_instance.load_vacancies(search_query)
        vacancies = hh_instance.get_vacancies()
        json_saver.save(vacancies)
    elif action == "2":
        n = int(input("Введите количество вакансий: "))
        vacancies = json_saver.load()
        sorted_vacancies = sorted(vacancies, key=lambda x: get_min_salary(x["salary"]), reverse=True)[:n]
        pprint(sorted_vacancies)
    elif action == "3":
        keyword = input("Введите ключевое слово: ")
        vacancies = json_saver.load()
        filtered_vacancies = [vacancy for vacancy in vacancies if keyword in vacancy["description"]]
        pprint(filtered_vacancies)
    elif action == "4":
        print("До свидания!")
    else:
        print("Неверный ввод. Пожалуйста, выберите действие от 1 до 4.")

def get_min_salary(salary):
    """
    Получает минимальную зарплату из словаря зарплаты.

    Args:
        salary (dict): Словарь с данными о зарплате.

    Returns:
        float: Минимальная зарплата.
    """
    min_salary = 0
    if salary:
        if salary.get("from") is not None and salary.get("to") is not None:
            min_salary = (salary["from"] + salary["to"]) / 2
        elif salary.get("from") is not None:
            min_salary = salary["from"]
        elif salary.get("to") is not None:
            min_salary = salary["to"]
    return min_salary