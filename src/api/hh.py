import os
from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class HeadHunter(API):
    token = os.getenv("HH_TOKEN")

    def get_vacancies(self, keyword: str, area=None, page=None, per_page=50):

        params = {'text': keyword,
                  'area': area,
                  'page': page,
                  'per_page': per_page
                  }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params).json()
        return response

    def get_required_data(self):
        pass


if __name__ == '__main__':
    print(HeadHunter().get_vacancies("python"))
