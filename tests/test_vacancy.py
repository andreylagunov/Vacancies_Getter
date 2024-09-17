from src.vacancy import Vacancy
# import json
import pytest



def test__init__(get_vacancy_obj):
    vacancy = get_vacancy_obj
    assert vacancy.speciality == "C++"
    assert vacancy.requirements == "cmake"
    assert vacancy.salary_str == "От 50000 до 200000 руб"
    assert vacancy.salary_dict == {"from": 50000, "to": 200000, "currency": "RUR"}
    assert vacancy.https_path == "www"


def test__eq__(get_vacancy_obj):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj
    assert vacancy_1 == vacancy_2


def test__ne__(get_vacancy_obj, get_vacancy_obj_2):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj_2
    assert vacancy_1 != vacancy_2


def test__gt__(get_vacancy_obj, get_vacancy_obj_2):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj_2
    assert vacancy_1 > vacancy_2


def test__lt__(get_vacancy_obj, get_vacancy_obj_2):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj_2
    assert vacancy_2 < vacancy_1


def test__ge__(get_vacancy_obj, get_vacancy_obj_2):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj_2
    assert vacancy_1 >= vacancy_2


def test__le__(get_vacancy_obj, get_vacancy_obj_2):
    vacancy_1 = get_vacancy_obj
    vacancy_2 = get_vacancy_obj_2
    assert vacancy_2 <= vacancy_1


def test__str__(get_vacancy_obj):
    vacancy = get_vacancy_obj
    # def __str__(self):
        # return f"{self.speciality}, {self.https_path}, {self.salary_str}, {self.requirements}"
    assert str(vacancy) == "C++, www, От 50000 до 200000 руб, cmake"


def test_cast_to___objects_list(get_vacancies_dicts__in_list):
    # with open("./data/vacancies_example.json", "r", encoding="utf-8") as file:
    #     json_data = json.load(file)
    initial_vacancies = get_vacancies_dicts__in_list
    vacancies_objects_list = Vacancy.cast_to___objects_list(initial_vacancies)
    assert str(vacancies_objects_list[0]) == "Аналитик данных (Data Analyst) г. Ташкент, https://api.hh.ru/vacancies/107300510?host=hh.ru, ЗП не указана, SQL для сложных и производительных запросов (CTE, оконные функции). <highlighttext>Python</highlighttext> для анализа данных (pandas, numpy). Опыт работы с инструментами бизнес..."
    assert str(vacancies_objects_list[1]) == "Бэкенд-разработчик Python Django, https://api.hh.ru/vacancies/106109534?host=hh.ru, От 80000 до 120000 руб, Опыт работы с Django Framework, Rest Framework и базами данных (PostgreSQL). Умение разбираться в чужом коде. Быть в состоянии выдержать..."
    assert str(vacancies_objects_list[2]) == "Младший программист, https://api.hh.ru/vacancies/107057173?host=hh.ru, ЗП не указана, Базовое знания любого языка программирования. Алгоритмическая/ Математическая база. Базовое знание университетской физики будет плюсом."
    assert str(vacancies_objects_list[3]) == "Junior Python, https://api.hh.ru/vacancies/107347408?host=hh.ru, ЗП не указана, Опыт программирования от 0,5 года с <highlighttext>Python</highlighttext> и\или JS. Опыт работы с каким-то из инструментов Jmeter/gatling..."
    assert str(vacancies_objects_list[4]) == "Back-end разработчик, https://api.hh.ru/vacancies/107368643?host=hh.ru, ЗП не указана, Знание в области информационных технологий или аналогичной области. Знание <highlighttext>Python</highlighttext> (и Django), PostgreSQL. Опыт работы с реляционными базами данных, включая..."


def test__get_salary_str___from_dict():
    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": {"from": 30000, "to": 60000, "currency": "RUR"}})
    assert salary_str == "От 30000 до 60000 руб"

    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": {"from": 3000, "to": 6000, "currency": "USD"}})
    assert salary_str == "От 3000 до 6000 USD"

    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": None})
    assert salary_str == "ЗП не указана"

    salary_str = Vacancy.test__get_salary_str___from_dict({"requirements": "cmake"})
    assert salary_str == "ЗП не указана"

    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": {"from": None, "to": 60000, "currency": "RUR"}})
    assert salary_str == "До 60000 руб"

    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": {"from": 30000, "to": None, "currency": "RUR"}})
    assert salary_str == "От 30000 руб"

    salary_str = Vacancy.test__get_salary_str___from_dict({"salary": {"from": 30000, "to": 60000, "currency": None}})
    assert salary_str == "От 30000 до 60000 (валюта не указана)"


def test__get_salary_dict___from_dict():
    salary_dict = Vacancy.test__get_salary_dict___from_dict({"salary": {"from": 30000, "to": 60000, "currency": "RUR"}})
    assert salary_dict == {"from": 30000, "to": 60000, "currency": "RUR"}

    salary_dict = Vacancy.test__get_salary_dict___from_dict({"salary": None})
    assert salary_dict == {"from": 0, "to": 0, "currency": ""}

    salary_dict = Vacancy.test__get_salary_dict___from_dict({"requirements": "cmake"})
    assert salary_dict == {"from": 0, "to": 0, "currency": ""}

    salary_dict = Vacancy.test__get_salary_dict___from_dict({"salary": {"from": None, "to": 60000, "currency": "RUR"}})
    assert salary_dict == {"from": 0, "to": 60000, "currency": "RUR"}

    salary_dict = Vacancy.test__get_salary_dict___from_dict({"salary": {"from": 30000, "to": None, "currency": "RUR"}})
    assert salary_dict == {"from": 30000, "to": 0, "currency": "RUR"}

    salary_dict = Vacancy.test__get_salary_dict___from_dict({"salary": {"from": 30000, "to": 60000, "currency": None}})
    assert salary_dict == {"from": 30000, "to": 60000, "currency": ""}


def test__is_speciality_valid(get_vacancy_obj):
    normal_vacancy = get_vacancy_obj
    assert normal_vacancy.speciality == "C++"

    with pytest.raises(TypeError) as exc_info:
        faulty_vacancy = Vacancy(333, "cmake", "От 50000 до 200000 руб", {"from": 50000, "to": 200000, "currency": "RUR"}, "www")
    assert str(exc_info.value) == "При проверке атрибута speciality: Не тип str."


def test__is_requirements_valid(get_vacancy_obj):
    normal_vacancy = get_vacancy_obj
    assert normal_vacancy.requirements == "cmake"

    with pytest.raises(TypeError) as exc_info:
        faulty_vacancy = Vacancy("C++", 222, "От 50000 до 200000 руб", {"from": 50000, "to": 200000, "currency": "RUR"}, "www")
    assert str(exc_info.value) == "При проверке атрибута requirements: Не тип str."


def test__is_salary_dict_valid(get_vacancy_obj):
    normal_vacancy = get_vacancy_obj
    assert normal_vacancy.salary_dict == {"from": 50000, "to": 200000, "currency": "RUR"}

    with pytest.raises(TypeError) as exc_info:
        faulty_vacancy = Vacancy("C++", "cmake", "От 50000 до 200000 руб", 222, "www")
    assert str(exc_info.value) == "При проверке атрибута salary_dict: Не тип dict[str, int]."


def test__is_salary_str_valid(get_vacancy_obj):
    normal_vacancy = get_vacancy_obj
    assert normal_vacancy.salary_str == "От 50000 до 200000 руб"

    with pytest.raises(TypeError) as exc_info:
        faulty_vacancy = Vacancy("C++", "cmake", None, {"from": 50000, "to": 200000, "currency": "RUR"}, "www")
    assert str(exc_info.value) == "При проверке атрибута salary_str: Не тип str."


def test__is_https_path_valid(get_vacancy_obj):
    normal_vacancy = get_vacancy_obj
    assert normal_vacancy.https_path == "www"

    with pytest.raises(TypeError) as exc_info:
        faulty_vacancy = Vacancy("C++", "cmake", "От 50000 до 200000 руб", {"from": 50000, "to": 200000, "currency": "RUR"}, None)
    assert str(exc_info.value) == "При проверке атрибута https_path: Не тип str."
