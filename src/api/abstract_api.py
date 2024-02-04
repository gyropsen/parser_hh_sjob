from abc import ABC, abstractmethod


class API(ABC):
    token = None

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    # @abstractmethod
    # def get_required_data(self,  data: dict):
    #     pass
