import unittest

from src.api.hh import HeadHunter


class TestGetData(unittest.TestCase):
    def test_get_vacancies(self):
        data = HeadHunter().get_vacancies("Повар")
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
