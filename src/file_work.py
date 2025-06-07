from abc import ABC, abstractmethod
import json


class FileWorker(ABC):
    """Абстрактный класс для работы с файлами"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Абстрактный метод для добавления вакансии в файл"""
        pass


    @abstractmethod
    def get_vacancies(self):
        """Получает вакансии из файла"""
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаляет информацию о вакансии из файла"""
        pass


class JSONSaver(FileWorker):
    """Класс для работы с JSON файлами"""
    def __init__(self, filename="../course_work2/data/vacancies.json"):
        """Инициализация класса"""
        self.__filename = filename


    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл"""
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies, file, ensure_ascii=False, indent=4)


    def get_vacancies(self):
        """Получает вакансии из JSON-файла"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def delete_vacancy(self, vacancy):
        """Метод для удаления вакансии из файла"""
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v != vacancy]
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)