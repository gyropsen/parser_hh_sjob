import unittest

from src.api.sjob import SuperJob


class TestGetData(unittest.TestCase):
    def test_get_vacancies(self):
        data = SuperJob().get_vacancies("Повар")
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
