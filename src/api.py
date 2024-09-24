from abc import ABC, abstractmethod

# from src.vacancy import Vacancy
import requests


class ConnectionByAPI(ABC):
    """Абстрактный класс для класса подключения к HeadHunter API"""

    @abstractmethod
    def __init__(self):
        """Конструктор экземпляра обработчика запросов к hh."""
        pass

    @abstractmethod
    def is_connection_good(self) -> bool:
        """
        Обёртка над приватным методом подключения к API hh.
        Возвращает True, если запрос на базовый URL - успешен.
        """
        pass

    @abstractmethod
    def get_vacancies_data(self, keyword: str, per_page: int, to_page: int) -> None:
        """
        Принимает:  ключевое слово для поиска вакансий,
        Формирует параметры для запроса из 'text', 'per_page',
        Отправляет запрос для получения данных о вакансиях по ключ.слову.
        """
        pass


class HeadHunterAPI(ConnectionByAPI):
    """Класс для работы с API HeadHunter"""

    __url: str
    __headers: dict[str, str]
    __params: dict[str, str | int]
    vacancies: list[dict]

    def __init__(self):
        """Конструктор экземпляра обработчика запросов к hh."""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 10}
        self.vacancies = []

    def get_dict_of_attributes(self) -> dict[str, str | dict | list]:
        """Служит для доступа на чтение к атрибутам экземпляра."""

        return {"url": self.__url, "headers": self.__headers, "params": self.__params, "vacancies": self.vacancies}

    def __check_connection(self) -> bool:
        """Отправляет запрос на базовый URL. Проверяет ответ."""

        response = requests.get(self.__url)
        code: int = response.status_code
        # print(f"__check_connection:  Статус код - {code}")
        if code == 200:
            return True
        return False

    def is_connection_good(self) -> bool:
        """
        Обёртка над приватным методом подключения к API hh.
        Возвращает True, если запрос на базовый URL - успешен.
        """
        return self.__check_connection()

    def get_vacancies_data(self, keyword: str, per_page: int, to_page: int) -> None:
        """
        Принимает:  ключевое слово для поиска вакансий,
        Формирует параметры для запроса из 'text', 'per_page',
        Отправляет запрос для получения данных о вакансиях по ключ.слову.
        """
        # На каждый вызов функции - очистка списка вакансий.
        self.vacancies = []

        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        if self.__check_connection():
            while self.__params.get("page") != to_page:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.__params["page"] += 1
            self.__params["page"] = 0


# if __name__ == "__main__":
#     hh_handler: HeadHunterAPI = HeadHunterAPI()
# print(hh_obj.__class__)
# hh_handler.is_connection_good()

# hh_handler.get_vacancies_data("Python", 8)
# print("len(hh_handler.vacancies):  ", len(hh_handler.vacancies))
# print("type(hh_handler.vacancies):  ", type(hh_handler.vacancies))
# print("type(hh_handler.vacancies[1]):  ", type(hh_handler.vacancies[1]))
# for vac in hh_handler.vacancies:
#     print(vac)

# print("=" * 50)
#
# vac_list = hh_obj.get_vacancies("Python")
# for vac in vac_list:
#     print(vac)

# vac_obj_list: list[Vacancy] = Vacancy.cast_to___objects_list(hh_handler.vacancies)
# for vac in vac_obj_list:
#     print(vac)
