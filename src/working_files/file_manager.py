import os
from src.working_files.abc_file_manager import WorkingFiles
import pandas as pd


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

    def in_file(self, vacancies_list: list[dict]) -> None:
        """
        Запись csv файла
        :param vacancies_list: список с вакансиями, представленные в виде словаря
        :return: None
        """
        df = pd.DataFrame.from_records(vacancies_list)
        df.to_csv(self.path, mode="a", encoding="utf-8", header=False, index=False)

    def out_file(self, keyword=None) -> list[dict]:
        """
        Сортировка по зарплате
        :param keyword: столбец в датафрейме
        :return: топ 5 операций
        """
        try:
            vacancies = pd.read_csv(self.path)
            top_vacancies_by_salary = vacancies.sort_values(by=keyword, ascending=False)[:5].to_dict("records")
            return top_vacancies_by_salary

        # Если нет keyword, то возвращаем список с пустым словарем
        except KeyError:
            return [{}]

    def del_file(self) -> None:
        """
        Удаляет файл с вакансиями
        :return: None
        """
        os.remove(self.path)


if __name__ == '__main__':
    filemanager = FileManager()
    filemanager.create_file()
    filemanager.in_file(
        [{"profession": "Data Analyst", "requirement": "работать", "address": "Moscow", "currency": "rub",
          "client_name": "sber",
          "link_client": "https://www.sber.ru", "link_vacancy": "https://www.sber.ru", "payment_from": 100,
          "payment_to": 100,
          "average_payment": 100}])
    print(filemanager.out_file("average_payment"))
    filemanager.del_file()
