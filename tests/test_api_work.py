import unittest
from unittest.mock import patch, MagicMock
from src.api_work import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    @patch('src.api_work.requests.get')
    def test_get_vacancies_loads_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'items': [{'id': 1, 'name': 'Vacancy 1'}, {'id': 2, 'name': 'Vacancy 2'}]
        }
        mock_get.return_value = mock_response

        api = HeadHunterAPI(file_worker=None)


        api.get_vacancies('Python Developer')

        self.assertEqual(len(api.vacancies), 40)
        self.assertEqual(api.vacancies[0]['name'], 'Vacancy 1')
        self.assertEqual(api.vacancies[1]['name'], 'Vacancy 2')

        self.assertEqual(mock_get.call_count, 20)

        args, kwargs = mock_get.call_args
        self.assertIn('params', kwargs)
        self.assertEqual(kwargs['params']['text'], 'Python Developer')

if __name__ == '__main__':
    unittest.main()