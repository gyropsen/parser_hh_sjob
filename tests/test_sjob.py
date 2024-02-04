from unittest.mock import patch
from src.api.sjob import SuperJob


@patch('requests.get')
def test_get_vacancies(mock_get):
    mock_get.return_value.json.return_value = {"name": "test", "id": 12}
    assert SuperJob().get_vacancies('testuser') == {"name": "test", "id": 12}
