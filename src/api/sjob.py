import os
from dotenv import load_dotenv
import requests
from src.api.abstract_api import API

load_dotenv()


class SuperJob(API):
    token = os.getenv("SJOB_TOKEN")

    def get_vacancies(self, keyword: str):
        headers = {'X-Api-App-Id': self.token}
        params = {'keyword': keyword,
                  "sort_new": 1,
                  'order_field': "date",
                  # 'order_direction': "desc",
                  # "payment_from": 100_000
                  }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params).json()
        return response


if __name__ == '__main__':
    print(SuperJob().get_vacancies("Python"))
