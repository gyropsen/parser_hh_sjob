from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class HeadHunter(API):
    def get_vacancies(self, text: str):
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
        vacancies_list = []
        for i, vacancy in enumerate(vacancies):
            data_vacancy = {"_id_": i,
                            "profession": vacancy["name"],
                            "requirement": vacancy["snippet"]["requirement"]
                            .replace("<highlighttext>", "").replace("</highlighttext>", "")
                            if vacancy["snippet"]["requirement"] else None,
                            "address": vacancy["address"]["raw"] if vacancy["address"] else None,
                            "currency": vacancy["salary"]["currency"] if vacancy["salary"] else None,
                            "client_name": vacancy["employer"]["name"],
                            "link_client": vacancy["employer"]["alternate_url"]
                            if vacancy["employer"].get("alternate_url") else None,
                            "link": vacancy["alternate_url"],
                            "payment_from": vacancy["salary"]["from"] if vacancy["salary"] else 0,
                            "payment_to": vacancy["salary"]["to"] if vacancy["salary"] else 0,
                            }
            vacancies_list.append(data_vacancy)
        return vacancies_list


if __name__ == '__main__':
    print(HeadHunter().get_vacancies("python"))
