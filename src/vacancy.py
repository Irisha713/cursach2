from dataclasses import asdict, dataclass
from functools import total_ordering


@total_ordering
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


    def __lt__(self, other):
        """Сравнение вакансий по зарплате (<)"""
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy")
        return self.salary < other.salary


    def __eq__(self, other):
        """Сравнение вакансий по зарплате (==)"""
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy")
        return self.salary == other.salary
