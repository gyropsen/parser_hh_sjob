import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancies():
    vc1 = Vacancy(1, "Data Analyst", "Сказочное Бали", "RUB",
                  "Isixi Private Limited",
                  "https://www.jobstreet.co.id/job/72697729?type=standard&ref=search-"
                  "standalone#sol=4df3b84bef39026898b572d9d5c8201567f979c7",
                  80_000, 0)
    vc2 = Vacancy(2, "python backend developer", "Moscow", "RUB",
                  "SBER", "https://www.sber.ru", 60_000, 90_000)

    vc3 = Vacancy(2, "python backend developer", "Moscow", "RUB",
                  "SBER", "https://www.sber.ru", 0, 90_000)

    return vc1, vc2, vc3


def test_verification():
    with pytest.raises(ValueError):
        Vacancy()


def test_vacancy(vacancies):
    assert vacancies[0] > vacancies[1]


def test_change_average_payment(vacancies):
    assert vacancies[0].average_payment == 80_000
    assert vacancies[1].average_payment == 75_000
    assert vacancies[2].average_payment == "По договоренности"
