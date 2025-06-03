from dataclasses import asdict, dataclass


@dataclass
class Vacancy:
    """Класс для предоставления вакансии"""
    title: str
    url: str
    salary: int = 0
    description: str = ""


    def to_dict(self):
        """Преобразует объект Vacancy в словарь"""
        return asdict(self)


    def check_salary(self):
        """Проверка указания зарплаты"""
        if not self.salary:
            self.salary = 0


    def comparison(self, other):
        """Сравнение зарплат у вакансий"""
        return self.salary < other.salary


