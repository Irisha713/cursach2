import unittest
from src.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy(
            title="Разработчик",
            url="https://example.com/vacancy1",
            salary=1000,
            description="Описание вакансии 1"
        )
        self.vacancy2 = Vacancy(
            title="Аналитик",
            url="https://example.com/vacancy2",
            salary=2000,
            description="Описание вакансии 2"
        )
        self.vacancy_no_salary = Vacancy(
            title="Менеджер",
            url="https://example.com/vacancy3",
            salary=None,
            description="Описание вакансии 3"
        )


    def test_to_dict(self):
        vacancy_dict = self.vacancy1.to_dict()
        expected_dict = {
            "title": "Разработчик",
            "url": "https://example.com/vacancy1",
            "salary": 1000,
            "description": "Описание вакансии 1"
        }
        self.assertEqual(vacancy_dict, expected_dict)


    def test_check_salary_with_salary(self):
        self.vacancy1.check_salary()
        self.assertEqual(self.vacancy1.salary, 1000)


    def test_check_salary_without_salary(self):
        self.vacancy_no_salary.check_salary()
        self.assertEqual(self.vacancy_no_salary.salary, 0)


    def test_comparison_salary_less(self):
        result = self.vacancy1.comparison(self.vacancy2)
        self.assertTrue(result)


    def test_comparison_salary_equal(self):
        vacancy_same_salary = Vacancy(
            title="Копия вакансии 1",
            url="https://example.com/vacancy4",
            salary=1000,
            description="Описание"
        )
        result = self.vacancy1.comparison(vacancy_same_salary)
        self.assertFalse(result)


    def test_comparison_salary_greater(self):
        result = self.vacancy2.comparison(self.vacancy1)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()