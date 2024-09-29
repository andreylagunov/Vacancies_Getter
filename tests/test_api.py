from src.api import HeadHunterAPI


def test__init__():
    hh_handler: HeadHunterAPI = HeadHunterAPI()
    assert type(hh_handler) is HeadHunterAPI
    assert hh_handler.get_dict_of_attributes() == {
        "url": 'https://api.hh.ru/vacancies',
        "headers": {'User-Agent': 'HH-User-Agent'},
        "params": {'text': '', 'page': 0, 'per_page': 10},
        "vacancies": []
    }


def test_is_connection_good():
    hh_handler: HeadHunterAPI = HeadHunterAPI()
    response = hh_handler.is_connection_good()
    assert response is True or response is False


def test_get_vacancies_data():
    hh_handler: HeadHunterAPI = HeadHunterAPI()
    hh_handler.get_vacancies_data("Python", 8, 2)

    vacancies_list: list = hh_handler.get_dict_of_attributes()["vacancies"]
    if len(vacancies_list):
        assert hh_handler.is_connection_good() is True
        assert len(vacancies_list) == 16
        assert type(vacancies_list) is list
        assert type(vacancies_list[1]) is dict
        test_dict = vacancies_list[1]
        assert "id" in test_dict and "name" in test_dict and "salary" in test_dict
    else:
        assert hh_handler.is_connection_good() is False
        assert vacancies_list == []
