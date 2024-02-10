import os
import pandas as pd

from src.working_files.abc_file_manager import WorkingFiles
from src.vacancy import Vacancy


class FileManager(WorkingFiles):
    """
    Класс для работы с файлами
    """

    def create_file(self) -> None:
        """
        Если не создан файл, создает csv файл vacancies.csv
        :return: None
        """
        if not os.path.exists(self.path):
            clear_dataframe = {"profession": [], "requirement": [], "address": [], "currency": [],
                               "client_name": [],
                               "link_client": [], "link_vacancy": [], "payment_from": [], "payment_to": [],
                               "average_payment": []}
            df = pd.DataFrame(clear_dataframe)
            df.to_csv(self.path, encoding="utf-8", index=False)

    def in_file(self, vacancies_cls_list: list) -> None:
        """
        Запись csv файла
        :param vacancies_cls_list: список с вакансиями, представленные в виде объектов Vacancy
        :return: None
        """
        df = pd.DataFrame.from_records([vacancy.__dict__ for vacancy in vacancies_cls_list])
        df.to_csv(self.path, mode="a", encoding="utf-8", header=False, index=False)

    def out_file(self) -> list[dict]:
        """
        Получаем вакансии из файла
        :return: список со словарями вакансий
        """
        try:
            vacancies = pd.read_csv(self.path, keep_default_na=False)
            vacancies = vacancies.to_dict("records")
            return vacancies
        except FileNotFoundError:
            return [{}]

    def del_file(self) -> None:
        """
        Удаляет файл с вакансиями
        :return: None
        """
        os.remove(self.path)

    @staticmethod
    def cast_to_object_list(vacancies_dict_list: list[dict]) -> list[Vacancy]:
        vacancies_cls_list = [Vacancy(profession=vacancies_json["profession"],
                                      requirement=vacancies_json["requirement"],
                                      address=vacancies_json["address"],
                                      currency=vacancies_json["currency"],
                                      client_name=vacancies_json["client_name"],
                                      link_client=vacancies_json["link_client"],
                                      link_vacancy=vacancies_json["link"],
                                      payment_from=vacancies_json["payment_from"],
                                      payment_to=vacancies_json["payment_to"]
                                      ) for vacancies_json in vacancies_dict_list]
        return vacancies_cls_list


if __name__ == '__main__':
    pass
