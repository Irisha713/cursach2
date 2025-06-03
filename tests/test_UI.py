import unittest
from src.vacancy import Vacancy
from src.UI import (
    convert_to_vacancy_objects,
    filter_vacancies,
    get_vacancies_by_salary,
    get_top_vacancies,
)

class TestVacancyFunctions(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy("Developer", "http://example.com/1", 100000, "Responsibilities include coding")
        self.vacancy2 = Vacancy("Manager", "http://example.com/2", 150000, "Manage team and responsibilities")
        self.vacancy3 = Vacancy("Designer", "http://example.com/3", None, "Design interfaces")
        self.vacancy4 = Vacancy("QA", "http://example.com/4", "не указана", "Testing software")
        self.vacancies = [self.vacancy1, self.vacancy2, self.vacancy3, self.vacancy4]


    def test_convert_to_vacancy_objects(self):
        vacancies_data = [
            {
                "name": "Developer",
                "alternate_url": "http://example.com/1",
                "salary": {"from": 100000},
                "snippet": {"responsibility": "Responsibilities include coding"}
            },
            {
                "name": "Manager",
                "alternate_url": "http://example.com/2",
                "salary": {"from": 150000},
                "snippet": {"responsibility": "Manage team and responsibilities"}
            },
            {
                "name": "Designer",
                "alternate_url": "http://example.com/3",
                "salary": None,
                "snippet": {"responsibility": "Design interfaces"}
            }
        ]
        result = convert_to_vacancy_objects(vacancies_data)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].title, "Developer")
        self.assertEqual(result[1].salary, 150000)
        self.assertIsNone(result[2].salary)


    def test_filter_vacancies(self):
        filter_words = ["coding", "manage"]
        filtered = filter_vacancies(self.vacancies, filter_words)
        self.assertIn(self.vacancy1, filtered)
        self.assertIn(self.vacancy2, filtered)
        self.assertNotIn(self.vacancy3, filtered)
        self.assertNotIn(self.vacancy4, filtered)


    def test_get_vacancies_by_salary_range(self):
        result = get_vacancies_by_salary(self.vacancies, "90000-160000")
        self.assertIn(self.vacancy1, result)
        self.assertIn(self.vacancy2, result)
        self.assertNotIn(self.vacancy3, result)
        self.assertNotIn(self.vacancy4, result)

        all_vacancies = get_vacancies_by_salary(self.vacancies, "")
        self.assertEqual(all_vacancies, self.vacancies)

        result_none = get_vacancies_by_salary(self.vacancies, "200000-300000")
        self.assertEqual(result_none, [])


    def test_get_top_vacancies(self):
        top = get_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top, self.vacancies[:2])

if __name__ == '__main__':
    unittest.main()