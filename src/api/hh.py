from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class HeadHunter(API):
    """
    Класс для работы с вакансиями HeadHunter
    """

    def get_vacancies(self, text: str):
        """
        Получение вакансий
        :param text: Ключевое слово
        :return: вызов функции get_json_vacancy
        """
        vacancies = []
        params = {'text': text,
                  'page': 0,
                  'per_page': 100,
                  'salary': 60000,
                  'currency': "RUR",

                  }
        count_pages = 2
        while params["page"] < count_pages:
            response_again = requests.get('https://api.hh.ru/vacancies', params=params).json()

            count_pages = response_again["pages"]
            params["page"] += 1
            for json_vacancy in self.get_json_vacancy(response_again["items"]):
                vacancies.append(json_vacancy)
        return vacancies

    @staticmethod
    def get_json_vacancy(vacancies: list):
        """
        Преобразование одного json в другой
        :param vacancies: список словаря с вакансиями
        :return: список словаря с вакансиями
        """
        vacancies_list = []

        if not vacancies:
            return vacancies_list
        for vacancy in vacancies:
            data_vacancy = {
                "profession": vacancy["name"],
                "requirement": vacancy["snippet"]["requirement"]
                .replace("<highlighttext>", "").replace("</highlighttext>", "")
                if vacancy["snippet"]["requirement"] else "",
                "address": vacancy["address"]["raw"] if vacancy.get("address") == "None" else "",
                "currency": vacancy["salary"]["currency"] if vacancy["salary"] else "",
                "client_name": vacancy["employer"]["name"],
                "link_client": vacancy["employer"]["alternate_url"] if vacancy["employer"].get("alternate_url") else ""
                if vacancy["employer"].get("alternate_url") else "",
                "link": vacancy["alternate_url"],
            }
            if vacancy["salary"]:
                data_vacancy["payment_from"] = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                data_vacancy["payment_to"] = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            else:
                data_vacancy["payment_from"] = 0
                data_vacancy["payment_to"] = 0
            vacancies_list.append(data_vacancy)
        return vacancies_list


if __name__ == '__main__':
    print(HeadHunter().get_vacancies("Python backend developer"))
