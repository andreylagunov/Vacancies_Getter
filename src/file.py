import json
import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileHandler(ABC):
    """Абстрактный класс для класса работы с файлами (JSON)."""

    @abstractmethod
    def __init__(self, file_name: str):
        """
        В экземпляре есть атрибут - имя файла,
        которое может быть назначено при создании экземпляра.
        """
        pass

    @abstractmethod
    def get_data_from_file(self) -> list[dict]:
        """Метод получения данных из файла."""
        pass

    @abstractmethod
    def add_data_to_file(self, data_of_vacancy_type: Vacancy) -> None:
        """
        Метод добавления данных в файл.
        В JSON-файл сохраняются данные (атрибуты класса Vacancy) списком словарей.
        """
        pass

    @abstractmethod
    def delete_data_from_file(self, vacancy: Vacancy) -> None:
        """Метод удаления данных из файла."""
        pass


class JSONHandler(FileHandler):
    """Класс для работы с JSON-файлами."""

    __file_name: str
    __relative_file_path: str

    def __init__(self, file_name: str = "saved_vacancies.json"):
        """
        В экземпляре есть атрибут - имя файла,
        которое может быть назначено при создании экземпляра.
        """
        self.__file_name = file_name
        if __name__ == "__main__":
            self.__relative_file_path = f"../data/{file_name}"
        else:
            self.__relative_file_path = f"./data/{file_name}"

    def get_dict_of_attributes(self) -> dict[str, str]:
        """Возвращает словарь со значениями атрибутов экземпляра."""

        return {"file_name": self.__file_name, "relative_file_path": self.__relative_file_path}

    def __create_file_if_needed(self) -> None:
        """Создание файла для хранения вакансий, если его не существует"""

        if not os.path.exists(self.__relative_file_path):
            with open(self.__relative_file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

    def __read_file(self) -> list[dict]:
        """Чтение json-файла. Возврат списка словарей с вакансиями."""

        with open(self.__relative_file_path, "r", encoding="utf-8") as file:
            vacancy_list: list = json.load(file)
        return vacancy_list

    def __write_file(self, vacancy_list: list) -> None:
        """Запись в json-файл списка вакансий."""

        with open(self.__relative_file_path, "w", encoding="utf-8") as file:
            json.dump(vacancy_list, file, ensure_ascii=False)

    def get_data_from_file(self) -> list[dict]:
        """Возвращает список данных (вакансий) из файла."""

        self.__create_file_if_needed()
        return self.__read_file()

    def add_data_to_file(self, vacancy: Vacancy) -> None:
        """
        Метод добавления данных в файл.
        В JSON-файл сохраняются (добавляются) данные (атрибуты класса Vacancy) списком словарей.
        """

        vacancy_list: list = self.get_data_from_file()

        # Ищем дублирование. Если оно есть, завершаем выполнение (без добавления вакансии).
        for vacancy_dict in vacancy_list:
            if vacancy_dict["speciality"] == vacancy.speciality:
                return

        # Если дублирования не обнаружено, добавляем вакансию.
        vacancy_list.append(
            {
                "speciality": vacancy.speciality,
                "https_path": vacancy.https_path,
                "salary_str": vacancy.salary_str,
                "requirements": vacancy.requirements,
            }
        )

        # Записываем обновлённый список обратно в файл.
        self.__write_file(vacancy_list)

    def delete_data_from_file(self, vacancy: Vacancy) -> None:
        """Метод удаления данных (вакансии) из файла."""

        vacancy_list: list = self.get_data_from_file()

        deleted_vacancy_list: list = [
            vac_dict for vac_dict in vacancy_list if vac_dict["speciality"] != vacancy.speciality
        ]

        # Записываем обновлённый список обратно в файл.
        self.__write_file(deleted_vacancy_list)


if __name__ == "__main__":
    vac_1 = Vacancy("C++", "cmake", "От 50000 до 200000", {"from": 40000, "to": 25000, "currency": "RUR"}, "www")
    vac_2 = Vacancy("I am", "You are", "3 - 4", {"from": 30000, "to": 35000, "currency": "RUR"}, "www")
    vac_3 = Vacancy("Rust", "all", "От 3000 руб", {"from": 3000, "to": 0, "currency": "RUR"}, "www")

    jh = JSONHandler()
    # jh.add_data_to_file(vac_1)
    # jh.add_data_to_file(vac_2)
    # jh.delete_data_from_file(vac_1)
    jh.delete_data_from_file(vac_2)
    # jh.add_data_to_file(vac_3)

    # help(open)
    # ========= ===============================================================
    # Character Meaning
    # --------- ---------------------------------------------------------------
    # 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)
    # '+'       open a disk file for updating (reading and writing)
    # ========= ===============================================================

    # json_str = """
    # {
    #     "people": [
    #         {
    #             "name": "Ivan",
    #             "phone": "777"
    #         },
    #         {
    #             "name": "Irina",
    #             "phone": "963"
    #         }
    #     ]
    # }
    # """
    # Преобразование строкового json-формата в Python-объекты.
    # load   - загружаем в Python
    #     s  - строковый вариант
    # data = json.loads(json_str)
    # for man_dict in data["people"]:
    #     print(man_dict["phone"])
    #     man_dict["country"] = "Russia"

    # Преобразование Python-объектов в строку формата json.
    # dump   - выгружаем из Python
    #     s  - в строковый вариант
    # json_str_2 = json.dumps(data)
    # print("json_str_2:   ", json_str_2)
    # print("type(json_str_2)", type(json_str_2))

    # # Запись данных типа str в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump(json_str_2, file)

    # # Запись данных типа dict в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump(data, file)

    # # Запись данных типа list в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump([1, 2, "4", True], file)

    # # Запись данных типа tuple в файл (формата json) - в файле будет list.
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump((1, 2, "4", True), file)

    # # Запись данных типа str в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump("json_str_2 + !@#$%^&*~", file)

    # # Запись данных типа int в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump(321, file)

    # # Запись данных типа float в файл (формата json).
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump(321.999, file)

    # Чтение json-файла - т.е. преобразование содержимого файла в   Python - объект.
    # with open("../data/test_example.json", "r", encoding="utf-8") as j_file:
    #     python_data = json.load(j_file)
    # print("python_data:   ", python_data)
    # # {"people": [{"name": "Ivan", "phone": "777", "country": "Russia"},
    # # {"name": "Irina", "phone": "963", "country": "Russia"}]}
    #
    # print("type(python_data)):   ", type(python_data))

    # # Преобразование строкового формата в Python-типы:
    # python_data = json.loads(python_data_from_file___str)
    # print("python_data:   ", python_data)
    # # {'people': [{'name': 'Ivan', 'phone': '777', 'country': 'Russia'},
    # # {'name': 'Irina', 'phone': '963', 'country': 'Russia'}]}
    # print("type(python_data):   ", type(python_data))       # <class 'dict'>
    # for man_dict in python_data["people"]:
    #     man_dict["phone"] = f"+({man_dict["phone"]})"       # 'phone': '777'   --->     'phone': '+(777)'
    # print("python_data:   ", python_data)

    # # Запись полученного Python-объекта (python_data) обратно в файл (формата json):
    # with open("../data/test_example.json", "w", encoding="utf-8") as file:
    #     json.dump(python_data, file)

    # directory = os.getcwd().split("/")[-1]
    # print("os.getcwd() -> directory:  ", directory)

    # @staticmethod
    # def create_file(file_name: str) -> None:
    #     """ Создание файла для обработчика json """
    #
    #     directory = os.getcwd().split("/")[-1]
    #     # print("directory: ", directory)
    #     if directory == "VacanciesGetter":
    #         insertion = ""
    #     elif directory == "src":
    #         insertion = "../"
    #
    #     if os.path.exists(f"{insertion}data/{file_name}"):
    #         return
    #     else:
