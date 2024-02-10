from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @staticmethod
    def get_json_vacancy(vacancies: list):
        pass
