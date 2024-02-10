from src.working_files.file_manager import FileManager
import re

filemanager = FileManager()


def filter_by_keyword_salary(filter_word: str, top_n: int, salary_range: str) -> list[dict]:
    """
    Сортировка вакансий по ключевому слову и диапазону зарплаты
    :param filter_word: ключевое слово
    :param top_n: сколько вакансий вывести
    :param salary_range: диапазон зарплаты
    :return: кортеж списков с вакансиями
    """
    vacancies_json_list = filemanager.out_file()
    pattern = re.compile(filter_word)
    vacancies_by_keyword = [vacancy for vacancy in vacancies_json_list
                            if pattern.search(vacancy['profession'])
                            or pattern.search(vacancy['requirement'])]
    salary = salary_range.split("-")
    vacancies_by_salary = []
    vacancies_by_agreements = []
    for vacancy in vacancies_by_keyword:
        if vacancy["average_payment"] == "По договоренности":
            vacancies_by_agreements.append(vacancy)
        elif float(salary[0]) <= float(vacancy["average_payment"]) <= float(salary[1]):
            vacancies_by_salary.append(vacancy)
    vacancies_by_salary_top = sorted(vacancies_by_salary, key=lambda vacancy: vacancy["average_payment"])
    return vacancies_by_salary_top[:top_n-1]


if __name__ == '__main__':
    print(filter_by_keyword_salary("Python", 5, "10000-1000000"))
