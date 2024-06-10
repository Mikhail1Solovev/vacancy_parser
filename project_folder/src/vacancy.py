class Vacancy:
    def __init__(self, id, name, salary, city, street, description):
        """
        Инициализирует экземпляр Vacancy.

        Args:
            id (str): Идентификатор вакансии.
            name (str): Название вакансии.
            salary (dict): Информация о зарплате.
            city (str): Город.
            street (str): Улица.
            description (str): Описание вакансии.
        """
        self.id = id
        self.name = name
        self.salary = salary
        self.city = city
        self.street = street
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление вакансии.

        Returns:
            str: Строковое представление вакансии.
        """
        return f"Vacancy(id={self.id}, name={self.name}, salary={self.salary}, city={self.city}, street={self.street}, description={self.description})"

    def to_dict(self):
        """
        Преобразует объект Vacancy в словарь.

        Returns:
            dict: Словарь с данными вакансии.
        """
        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary,
            "city": self.city,
            "street": self.street,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        """
        Создает экземпляр Vacancy из словаря.

        Args:
            data (dict): Словарь с данными вакансии.

        Returns:
            Vacancy: Экземпляр класса Vacancy.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            salary=data.get("salary"),
            city=data.get("city"),
            street=data.get("street"),
            description=data.get("description")
        )
