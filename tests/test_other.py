from src.other import *


def test___get_salary_range_from_user():
    range = get_salary_range_from_user(is_in_test=True)
    assert range == {"from": 50000, "to": 90000, "currency": "RUR"}


def test___filter_vacancies(get_vacancy_obj, get_vacancy_obj_2):
    # filter_vacancies(vacancies_obj_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:

    c_vacancy = get_vacancy_obj
    python_vacancy = get_vacancy_obj_2
    vacancies_list = [c_vacancy, python_vacancy]
    filter_words = ["cmake"]
    assert filter_vacancies(vacancies_list, filter_words) == [c_vacancy]


def test___get_vacancies_by_salary(get_vacancy_obj, get_vacancy_obj_2):
    # get_vacancies_by_salary(vacancies_obj_list: list[Vacancy], salary_dict: dict[str, int | str]) -> list[Vacancy]:

    c_vacancy = get_vacancy_obj
    python_vacancy = get_vacancy_obj_2
    vacancies_list = [c_vacancy, python_vacancy]
    salary_dict = {"from": 30000, "to": 45000, "currency": "RUR"}
    assert get_vacancies_by_salary(vacancies_list, salary_dict) == [python_vacancy]


def test___sort_vacancies_by_magic_methods_inplace(get_vacancy_obj, get_vacancy_obj_2):
    # sort_vacancies_by_magic_methods_inplace(vacancies_obj_list: list[Vacancy]) -> list[Vacancy]:

    c_vacancy = get_vacancy_obj
    python_vacancy = get_vacancy_obj_2
    vacancies_list = [python_vacancy, c_vacancy]
    assert sort_vacancies_by_magic_methods_inplace(vacancies_list) == [c_vacancy, python_vacancy]


def test___get_top_vacancies(get_vacancy_obj, get_vacancy_obj_2):
    # get_top_vacancies(vacancies_obj_list: list[Vacancy], top_n: int) -> list[Vacancy]:

    c_vacancy = get_vacancy_obj
    python_vacancy = get_vacancy_obj_2
    vacancies_list = [python_vacancy, c_vacancy]
    assert get_top_vacancies(vacancies_list, 1) == [python_vacancy]
    assert get_top_vacancies(vacancies_list, 2) == [python_vacancy, c_vacancy]


def test___print_vacancies():
    pass


def test___final_save_vacancies_to_file():
    # final_save_vacancies_to_file(vacancies_obj_list: list[Vacancy]) -> None:
    pass
