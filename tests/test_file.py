from src.file import JSONHandler
from src.vacancy import Vacancy
# import os


def test__init__with_default_file_name():
    json_handler: JSONHandler = JSONHandler()
    test_dict = json_handler.get_dict_of_attributes()

    assert test_dict["file_name"] == "default_vacancies_file.json"

    # directory = os.getcwd().split("/")[-1]
    # if directory == "VacanciesGetter":
    assert test_dict["relative_file_path"] == "./data/default_vacancies_file.json"
    # else:
    #     assert test_dict["relative_file_path"] == "../data/saved_vacancies.json"


def test__init__with_user_file_name():
    json_handler: JSONHandler = JSONHandler("user_file_name.json")
    test_dict = json_handler.get_dict_of_attributes()

    assert test_dict["file_name"] == "user_file_name.json"
    assert test_dict["relative_file_path"] == "./data/user_file_name.json"


def test_get_dict_of_attributes():
    json_handler: JSONHandler = JSONHandler("user_file_name.json")
    test_dict = json_handler.get_dict_of_attributes()

    assert test_dict == {
        "file_name": "user_file_name.json",
        "relative_file_path": "./data/user_file_name.json"
    }


def test___add_data_to_file(get_vacancy_obj, get_vacancy_obj_2):
    vac_1: Vacancy = get_vacancy_obj
    vac_2: Vacancy = get_vacancy_obj_2
    json_h: JSONHandler = JSONHandler("saved_vacancies_from_pytest.json")

    # Предварительная очистка файла от вакансий (требуется для тестирования).
    json_h.delete_data_from_file(vac_1)
    json_h.delete_data_from_file(vac_2)

    json_h.add_data_to_file(vac_1)
    assert json_h.get_data_from_file() == [{
        "speciality": "C++",
        "https_path": "www",
        "salary_str": "От 50000 до 200000 руб",
        "requirements": "cmake"
    }]
    json_h.add_data_to_file(vac_2)
    assert json_h.get_data_from_file() == [{
        "speciality": "C++",
        "https_path": "www",
        "salary_str": "От 50000 до 200000 руб",
        "requirements": "cmake"
    },
    {
        "speciality": "Python",
        "https_path": "www",
        "salary_str": "От 40000 до 200000 руб",
        "requirements": "PyCharm"
    }]

    # При попытке повторного добавления такой же вакансии - файл неизменный.
    json_h.add_data_to_file(vac_2)
    assert json_h.get_data_from_file() == [{
        "speciality": "C++",
        "https_path": "www",
        "salary_str": "От 50000 до 200000 руб",
        "requirements": "cmake"
    },
    {
        "speciality": "Python",
        "https_path": "www",
        "salary_str": "От 40000 до 200000 руб",
        "requirements": "PyCharm"
    }]
    # Очистка файла перед последующими тестами.
    json_h.delete_data_from_file(vac_1)
    json_h.delete_data_from_file(vac_2)


def test___get_data_from_file(get_vacancy_obj):
    vac_1: Vacancy = get_vacancy_obj
    json_h: JSONHandler = JSONHandler("saved_vacancies_from_pytest.json")

    # Проверяем, что файл - пуст.
    assert json_h.get_data_from_file() == []

    # Добавляем вакансию в файл.
    json_h.add_data_to_file(vac_1)

    # Проверяем, что в файл она добавилась, о она - одна.
    assert json_h.get_data_from_file() == [{
        "speciality": "C++",
        "https_path": "www",
        "salary_str": "От 50000 до 200000 руб",
        "requirements": "cmake"
    }]
    # Очистка файла перед последующими тестами.
    json_h.delete_data_from_file(vac_1)

def test___delete_data_from_file(get_vacancy_obj):
    vac_1: Vacancy = get_vacancy_obj
    json_h: JSONHandler = JSONHandler("saved_vacancies_from_pytest.json")

    json_h.add_data_to_file(vac_1)
    # Проверка того, что в файле есть одна вакансия.
    assert json_h.get_data_from_file() == [{
        "speciality": "C++",
        "https_path": "www",
        "salary_str": "От 50000 до 200000 руб",
        "requirements": "cmake"
    }]

    json_h.delete_data_from_file(vac_1)
    # Проверка отсутствия вакансий в файле после удаления одной.
    assert json_h.get_data_from_file() == []