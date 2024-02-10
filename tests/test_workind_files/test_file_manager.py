import pytest
from pathlib import Path
import os

from src.working_files.file_manager import FileManager

path = Path(Path(__file__).parent.parent.parent, "data", "vacancies.csv")


@pytest.fixture
def get_data():
    return FileManager()


def test_create_file(get_data):
    get_data.create_file()
    assert os.path.exists(path)


def test_in_file_out_file(get_data):
    assert get_data.out_file() == [{}]
    get_data.in_file(
        [{"profession": "Data Analyst", "requirement": "работать", "address": "Moscow", "currency": "rub",
          "client_name": "sber",
          "link_client": "https://www.sber.ru", "link_vacancy": "https://www.sber.ru", "payment_from": 100,
          "payment_to": 100,
          "average_payment": 100}])
    assert get_data.out_file("average_payment") == [
        {"profession": "Data Analyst", "requirement": "работать", "address": "Moscow", "currency": "rub",
         "client_name": "sber",
         "link_client": "https://www.sber.ru", "link_vacancy": "https://www.sber.ru", "payment_from": 100,
         "payment_to": 100,
         "average_payment": 100}]


def test_del_file(get_data):
    get_data.del_file()
    assert not os.path.exists(path)
