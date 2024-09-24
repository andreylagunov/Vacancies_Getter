# import json
from typing import Any


class Vacancy:
    """
    Класс Вакансия.
    Служит для представления вакансии в виде пяти свойств.
    """

    __slots__ = ("speciality", "requirements", "salary_str", "salary_dict", "https_path")
    # speciality: str                   # "Python Developer"
    # requirements: str                 # "Python, Git, ..."
    # salary_dict: dict[str, int]       # {"from": 100_000, "to": 140_000, "currency": "RUR"}
    # salary_str: str                   # "От 100000 до 140000 RUR"
    # https_path: str                   # "<https://hh.ru/vacancy/123456>"

    @classmethod
    def __get_salary_str___from_dict(cls, vac: dict) -> str:
        """
        Принимает словарь-вакансию (с HeadHunter)
        Возвращает атрибут salary_str вида "От 100000 до 140000 RUR" для объекта Vacancy
        """
        salary_str = ""
        if "salary" in vac and vac["salary"]:

            # Если указана ЗП "От ...", записываем в строку salary_str
            if "from" in vac["salary"]:
                if type(vac["salary"]["from"]) is int:
                    from_ = vac["salary"]["from"]
                    salary_str += f"От {from_}"

            # Если указана ЗП "до ...", ДОзаписываем в строку salary_str
            if "to" in vac["salary"]:
                if type(vac["salary"]["to"]) is int:
                    to_ = vac["salary"]["to"]

                    if salary_str != "":
                        # Если уже была записана ЗП "От ...", дозаписываем "до" через пробел
                        salary_str += f" до {to_}"
                    else:
                        # Если указана только ЗП "До ...", пишем "до" без пробела с большой буквы.
                        salary_str += f"До {to_}"

            # Дописываем "RUR"/"KZT"/... в конце, если указана хоть какая то ЗП.
            # Для валюты "RUR" пишем "руб"
            if salary_str != "":
                currency = vac["salary"]["currency"]
                if type(currency) is str:
                    salary_str += f" {currency if currency != "RUR" else "руб"}"
                else:
                    salary_str += " (валюта не указана)"

        else:
            salary_str = "ЗП не указана"

        return salary_str

    @classmethod
    def test__get_salary_str___from_dict(cls, vac: dict) -> str:
        """Вспомогательный метод для тестирования."""
        return cls.__get_salary_str___from_dict(vac)

    @classmethod
    def __get_salary_dict___from_dict(cls, vac: dict) -> dict[str, int | str]:
        """
        Принимает словарь-вакансию (с HeadHunter)
        Возвращает атрибут salary_dict вида {"from": 100_000, "to": 140_000, "currency": "RUR"} для объекта Vacancy
        """
        if "salary" in vac and vac["salary"]:
            salary_dict = {
                "from": vac["salary"]["from"] if type(vac["salary"]["from"]) is int else 0,
                "to": vac["salary"]["to"] if type(vac["salary"]["to"]) is int else 0,
                "currency": vac["salary"]["currency"] if type(vac["salary"]["currency"]) is str else "",
            }
        else:
            salary_dict = {
                "from": 0,
                "to": 0,
                "currency": "",
            }
        return salary_dict

    @classmethod
    def test__get_salary_dict___from_dict(cls, vac: dict) -> dict:
        """Вспомогательный метод для тестирования."""
        return cls.__get_salary_dict___from_dict(vac)

    @classmethod
    def cast_to___objects_list(cls, vacancies_list: list[dict]) -> list:
        """
        Преобразование из списка со словарями   (с ключами "name", "snippet"/"requirement", "salary", "url")
        в список объектов типа Vacancy.
        """
        objects_list = []

        # Из каждого словаря формируем объект Vacancy:
        for vac in vacancies_list:

            # Формирование атрибута salary_dict для объекта Vacancy
            salary_dict = cls.__get_salary_dict___from_dict(vac)

            # Формирование атрибута salary_str для объекта Vacancy
            salary_str = cls.__get_salary_str___from_dict(vac)

            # Формирование атрибута requirement для объекта Vacancy
            req_value: str | None = vac["snippet"]["requirement"]
            requirement_str: str = req_value if type(req_value) is str else "Требования не указаны."

            # Формирование атрибута speciality для объекта Vacancy
            spec_value: str | None = vac["name"]
            speciality_str: str = spec_value if type(spec_value) is str else "Специальность не указана."

            # Формирование атрибута https_path для объекта Vacancy
            path_value: str | None = vac["url"]
            path_value_str: str = path_value if type(path_value) is str else "URL не указан."

            # Из словаря vac создаём объект Vacancy:
            # Vacancy(speciality, requirements, salary_str, salary_dict, https_path)
            objects_list.append(Vacancy(speciality_str, requirement_str, salary_str, salary_dict, path_value_str))

        return objects_list

    # Методы валидации данных при инициализации объекта Vacancy:
    def __is_speciality_valid(self, value: Any) -> bool:
        """Проверка типа для атрибута speciality."""

        if type(value) is str:
            return True
        raise TypeError("При проверке атрибута speciality: Не тип str.")

    def __is_requirements_valid(self, value: Any) -> bool:
        """Проверка типа для атрибута requirements."""

        if type(value) is str:
            return True
        raise TypeError("При проверке атрибута requirements: Не тип str.")

    def __is_salary_dict_valid(self, salary_dict: Any) -> bool:
        """Проверка типа для атрибута salary_dict."""

        if type(salary_dict) is dict:
            if "from" in salary_dict and "to" in salary_dict and "currency" in salary_dict:

                type_of_from = type(salary_dict["from"])
                type_of_to = type(salary_dict["to"])
                type_of_currency = type(salary_dict["currency"])

                if type_of_from is int and type_of_to is int and type_of_currency is str:
                    return True

        raise TypeError("При проверке атрибута salary_dict: Не тип dict[str, int].")

    def __is_salary_str_valid(self, value: Any) -> bool:
        """Проверка типа для атрибута salary_str."""

        if type(value) is str:
            return True
        raise TypeError("При проверке атрибута salary_str: Не тип str.")

    def __is_https_path_valid(self, value: Any) -> bool:
        """Проверка типа для атрибута https_path."""

        if type(value) is str:
            return True
        raise TypeError("При проверке атрибута https_path: Не тип str.")

    def __init__(
        self, speciality: str, requirements: str, salary_str: str, salary_dict: dict[str, int | str], https_path: str
    ):
        """Конструктор экземпляра класса Vacancy"""

        if self.__is_speciality_valid(speciality):
            self.speciality = speciality
        if self.__is_requirements_valid(requirements):
            self.requirements = requirements
        if self.__is_salary_str_valid(salary_str):
            self.salary_str = salary_str
        if self.__is_salary_dict_valid(salary_dict):
            self.salary_dict = salary_dict
        if self.__is_https_path_valid(https_path):
            self.https_path = https_path

    def __avrg_salaries(self, other) -> tuple[float]:
        """
        Общий метод для сравнения зарплат по их среднему значению.
        Возвращает средние ЗП двух объектов.
        """

        if self.__class__ is other.__class__:

            # Среднюю ЗП формируем исходя их указанной "зарплатной вилки",
            # если "вилка От и До" не указана, в среднюю ЗП пишем то, что указано.

            self_from = self.salary_dict["from"]
            self_to = self.salary_dict["to"]
            if self_to and self_from:
                self_avrg = (self_from + self_to) / 2
            elif self_from:
                self_avrg = self_from
            elif self_to:
                self_avrg = self_to

            other_from = other.salary_dict["from"]
            other_to = other.salary_dict["to"]
            if other_from and other_to:
                other_avrg = (other_from + other_to) / 2
            elif other_from:
                other_avrg = other_from
            elif other_to:
                other_avrg = other_to

            return self_avrg, other_avrg

        raise TypeError("Попытка сравнения зарплат у объектов различных типов.")

    # Методы сравнения зарплат:
    def __eq__(self, other) -> bool:
        """Метод сравнения зарплат: равны ли."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary == other_avrg_salary

    def __ne__(self, other) -> bool:
        """Метод сравнения зарплат: неравны ли."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary != other_avrg_salary

    def __lt__(self, other) -> bool:
        """Метод сравнения зарплат: меньше ли."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary < other_avrg_salary

    def __gt__(self, other) -> bool:
        """Метод сравнения зарплат: больше ли."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary > other_avrg_salary

    def __ge__(self, other) -> bool:
        """Метод сравнения зарплат: равны ли или больше."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary >= other_avrg_salary

    def __le__(self, other) -> bool:
        """Метод сравнения зарплат: равны ли или меньше."""

        self_avrg_salary, other_avrg_salary = self.__avrg_salaries(other)
        return self_avrg_salary <= other_avrg_salary

    def __str__(self) -> str:
        """Метод вывода информации (атрибутов экземпляра) для пользователя."""

        return f"{self.speciality}, {self.https_path}, {self.salary_str}, {self.requirements}"


# if __name__ == "__main__":

# with open("../data/vacancies_example.json", "r", encoding="utf-8") as file:
#     json_data = json.load(file)
#
# print("type(json_data)", type(json_data))
# print("len(json_data)", len(json_data))
#
# print("type(json_data[1])", type(json_data[1]))


# vac_1 = Vacancy("C++", "cmake", "От 50000 до 200000", {"from": 40000, "to": 25000, "currency": "RUR"}, "www")
# vac_2 = Vacancy("I am", "You are", "3 - 4", {"from": 30000, "to": 35000, "currency": "RUR"}, "www")
# #
# try:
#     vac_3 = Vacancy("I am", "You are", "5 - 6", {"from": "10005", "to": 20002, "currency": "RUR"}, "www")
# except TypeError as exc_info:
#     # print(exc_info)
#     # print("type(exc_info):  ", type(exc_info))
#     assert str(exc_info) == "При проверке атрибута salary_dict: Не тип dict[str, int]."
#
# try:
#     vac_4 = Vacancy("I am", "You are", "7 - 8", {"f": 10005, "to": 20002, "currency": "RUR"}, "www")
# except TypeError as exc_info:
#     assert str(exc_info) == "При проверке атрибута salary_dict: Не тип dict[str, int]."
# #
# print("Равны ли средние ЗП:", vac_1 == vac_2)
# print("Неравны ли средние ЗП:", vac_1 != vac_2)
#
# print("Меньше ли у vac_1:", vac_1 < vac_2)
# print("Больше ли у vac_1:", vac_1 > vac_2)
#
# print("vac_1 <= vac_2:", vac_1 <= vac_2)
# print("vac_1 >= vac_2:", vac_1 >= vac_2)
#
# try:
#     print(vac_1 == 2)
# except TypeError:
#     print("Несравнимые вещи")
