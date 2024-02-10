from src.api.hh import HeadHunter
from src.api.sjob import SuperJob
from src.working_files.file_manager import FileManager
from src.utils.selection_vacancies import filter_by_keyword_salary

filemanager = FileManager()


def user_interaction():
    search_query = input("Введите поисковый запрос: ")

    hh_vacancies = HeadHunter().get_vacancies(search_query)
    sjob_vacancies = SuperJob().get_vacancies(search_query)

    vacancies_dict_list = hh_vacancies + sjob_vacancies
    vacancies_cls_list = filemanager.cast_to_object_list(vacancies_dict_list)

    filemanager.create_file()
    filemanager.in_file(vacancies_cls_list)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000-150000

    filter_vacancies = filter_by_keyword_salary(filter_word, top_n, salary_range)
    print("-----TOP VACANCIES-----")
    close = ""
    for i in range(len(filter_vacancies)):
        if close == "q":
            break
        print(f"\n profession: {filter_vacancies[i]["profession"]}")
        print(f" requirement: {filter_vacancies[i]["requirement"]}")
        print(f" payment_from: {filter_vacancies[i]["payment_from"]}")
        print(f" payment_to: {filter_vacancies[i]["payment_to"]}")
        print(f" average_payment: {filter_vacancies[i]["average_payment"]}")
        close = input("Press <q> to exit, <Enter> to continue")
    print("Все вакансии показаны")


if __name__ == '__main__':
    user_interaction()
