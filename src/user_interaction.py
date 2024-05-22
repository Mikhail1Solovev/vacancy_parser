from src.hh_api import HH
from src.json_saver import JSONSaver
from pprint import pprint

def user_interaction():
    """
    Основная функция для взаимодействия с пользователем.
    """
    hh_instance = HH(1)  # Введите ваш area_id
    json_saver = JSONSaver("data/vacancies.json")

    while True:
        action = input(
            "1. Ввести поисковый запрос\n"
            "2. Получить топ N вакансий по зарплате\n"
            "3. Получить вакансии с ключевым словом в описании\n"
            "4. Выйти\n"
            "Выберите действие: "
        )

        if action == "1":
            search_query = input("Введите поисковый запрос: ")
            hh_instance.load_vacancies(search_query)
            vacancies = hh_instance.get_vacancies()
            json_saver.save(vacancies)
            print(f"Загружено {len(vacancies)} вакансий и сохранено в файл.")
        elif action == "2":
            n = int(input("Введите количество вакансий: "))
            vacancies = json_saver.load()
            sorted_vacancies = sorted(vacancies, key=lambda x: get_min_salary(x["salary"]), reverse=True)[:n]
            print(f"Топ {n} вакансий по зарплате:")
            for vacancy in sorted_vacancies:
                print_vacancy(vacancy)
        elif action == "3":
            keyword = input("Введите ключевое слово: ")
            vacancies = json_saver.load()
            filtered_vacancies = [vacancy for vacancy in vacancies if keyword in vacancy["description"]]
            print(f"Вакансии с ключевым словом '{keyword}':")
            for vacancy in filtered_vacancies:
                print_vacancy(vacancy)
        elif action == "4":
            print("До свидания!")
            break
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

def print_vacancy(vacancy):
    """
    Выводит информацию о вакансии в читаемом формате.

    Args:
        vacancy (dict): Словарь с данными о вакансии.
    """
    print(f"\nНазвание: {vacancy['name']}")
    print(f"Зарплата: от {vacancy['salary']['from']} до {vacancy['salary']['to']} {vacancy['salary']['currency']}")
    print(f"Город: {vacancy['city']}")
    print(f"Улица: {vacancy['street']}")
    print(f"Описание: {vacancy['description']}")
    print(f"URL: {vacancy['id']}\n")

if __name__ == "__main__":
    user_interaction()
