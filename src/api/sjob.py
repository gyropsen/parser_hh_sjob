import os
from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class SuperJob(API):
    """
    Класс для работы с вакансиями SuperJob
    """
    token = os.getenv("SJOB_TOKEN")

    def get_vacancies(self, keyword: str):
        """
        Получение вакансий
        :param keyword: Ключевое слово
        :return: вызов функции get_json_vacancy
        """
        headers = {'X-Api-App-Id': self.token}
        params = {'keyword': keyword}
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params).json()
        return self.get_json_vacancy(response.get("objects"))

    @staticmethod
    def get_json_vacancy(vacancies: list):
        """
        Преобразование одного json в другой
        :param vacancies: список словаря с вакансиями
        :return: список словаря с вакансиями
        """
        if not vacancies:
            return
        vacancies_list = []
        for i, vacancy in enumerate(vacancies):
            data_vacancy = {"_id_": i,
                            "profession": vacancy["profession"],
                            "requirement": vacancy["candidat"].replace("\n", ""),
                            "address": vacancy["address"],
                            "currency": vacancy["currency"],
                            "client_name": vacancy["client"].get("title"),
                            "link_client": vacancy["client"].get("url"),
                            "link": vacancy["link"],
                            "payment_from": vacancy["payment_from"],
                            "payment_to": vacancy["payment_to"]
                            }
            vacancies_list.append(data_vacancy)
        return vacancies_list


if __name__ == '__main__':
    print(SuperJob().get_vacancies("Повар"))
