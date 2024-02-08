import os
from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class SuperJob(API):
    token = os.getenv("SJOB_TOKEN")

    def get_vacancies(self, keyword: str):
        headers = {'X-Api-App-Id': self.token}
        params = {'keyword': keyword}
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params).json()
        print(response)
        return self.get_json_vacancy(response.get("objects"))

    @staticmethod
    def get_json_vacancy(vacancies: list):
        if not vacancies:
            return
        vacancies_list = []
        for i, vacancy in enumerate(vacancies):
            data_vacancy = {"_id_": i,
                            "profession": vacancy["profession"],
                            "requirement": vacancy["candidat"].replace("\n", ""),
                            # .replace("<highlighttext>", "").replace("</highlighttext>", "")
                            # if vacancy["snippet"]["requirement"] else None,
                            "address": vacancy["address"],  # if vacancy["address"] else None,
                            "currency": vacancy["currency"],
                            # vacancy["salary"]["currency"] if vacancy["salary"] else None,
                            "client_name": vacancy["client"].get("title"),
                            "link_client": vacancy["client"].get("url"),
                            # if vacancy["employer"].get("alternate_url") else None,
                            "link": vacancy["link"],
                            "payment_from": vacancy["payment_from"],  # if vacancy["salary"] else 0,
                            "payment_to": vacancy["payment_to"]  # if vacancy["salary"] else 0,
                            }
            vacancies_list.append(data_vacancy)
        return vacancies_list


if __name__ == '__main__':
    print(SuperJob().get_vacancies("Повар"))
