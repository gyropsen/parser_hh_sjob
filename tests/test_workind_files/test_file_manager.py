import pytest
from pathlib import Path
import os
from src.utils.selection_vacancies import filter_by_keyword_salary

from src.working_files.file_manager import FileManager

path = Path(Path(__file__).parent.parent.parent, "data", "vacancies.csv")

filemaneger = FileManager()


@pytest.fixture
def get_data_from_api():
    return [{"profession": "Data Analyst",
             "requirement": "работать",
             "address": "Moscow",
             "currency": "rub",
             "client_name": "sber",
             "link_client": "https://www.sber.ru",
             "link": "https://www.sber.ru",
             "payment_from": 100,
             "payment_to": 100}]


@pytest.fixture
def get_data_out_file():
    return [{"profession": "Data Analyst",
             "requirement": "работать",
             "address": "Moscow",
             "currency": "rub",
             "client_name": "sber",
             "link_client": "https://www.sber.ru",
             "link_vacancy": "https://www.sber.ru",
             "payment_from": 100,
             "payment_to": 100,
             "average_payment": 100}]


def test_create_file():
    filemaneger.create_file()
    assert os.path.exists(path)


def test_out_file():
    assert filemaneger.out_file() == []


def test_in_file(get_data_from_api, get_data_out_file):
    vacancies_cls_list = filemaneger.cast_to_object_list(get_data_from_api)
    filemaneger.in_file(vacancies_cls_list)

    assert filemaneger.out_file() == get_data_out_file


def test_filter_by_keyword_salary(get_data_out_file):
    assert filter_by_keyword_salary("Data", 5, "100-101") == get_data_out_file


def test_del_file():
    filemaneger.del_file()
    assert not os.path.exists(path)
