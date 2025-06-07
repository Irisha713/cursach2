from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def connect(self):
        """Абстрактный метод для подключения к API"""
        pass


    @abstractmethod
    def get_vacancies(self, keyword):
        """Абстрактный метод для получения вакансий"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter'а"""
    def __init__(self, file_worker):
        """Инициализация"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        self.file_worker = file_worker
        super().__init__()


    def connect(self):
        """Подключение к API HeadHunter'a"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        return response.json()


    def get_vacancies(self, keyword):
        """Загружает вакансии по ключевому слову"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            data = self.connect()
            vacancies = data['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1


    @property
    def vacancies(self):
        return self.__vacancies
