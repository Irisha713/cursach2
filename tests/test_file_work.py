import unittest
import tempfile
import os
import json
from src.file_work import JSONSaver


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.temp_file.name
        self.saver = JSONSaver(filename=self.filename)


    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass


    def test_get_vacancies_empty_file(self):
        self.temp_file.close()
        result = self.saver.get_vacancies()
        self.assertEqual(result, [])


    def test_get_vacancies_valid_json(self):
        data = [{"title": "Developer"}]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        result = self.saver.get_vacancies()
        self.assertEqual(result, data)


    def test_get_vacancies_invalid_json(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write('invalid json')
        result = self.saver.get_vacancies()
        self.assertEqual(result, [])


    def test_add_vacancy_new(self):
        initial_data = [{"title": "Tester"}]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(initial_data, file)

        new_vacancy = {"title": "Developer"}
        self.saver.add_vacancy(new_vacancy)

        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.assertIn(new_vacancy, data)
        self.assertIn({"title": "Tester"}, data)


    def test_add_vacancy_duplicate(self):
        data = [{"title": "Developer"}]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

        self.saver.add_vacancy({"title": "Developer"})
        with open(self.filename, 'r', encoding='utf-8') as file:
            data_after = json.load(file)
        self.assertEqual(data_after, data)


    def test_delete_vacancy_existing(self):
        data = [{"title": "Developer"}, {"title": "Tester"}]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

        self.saver.delete_vacancy({"title": "Developer"})
        with open(self.filename, 'r', encoding='utf-8') as file:
            result_data = json.load(file)
        self.assertNotIn({"title": "Developer"}, result_data)
        self.assertIn({"title": "Tester"}, result_data)


    def test_delete_vacancy_nonexistent(self):
        data = [{"title": "Tester"}]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

        self.saver.delete_vacancy({"title": "Developer"})
        with open(self.filename, 'r', encoding='utf-8') as file:
            result_data = json.load(file)
        self.assertEqual(result_data, data)

if __name__ == '__main__':
    unittest.main()