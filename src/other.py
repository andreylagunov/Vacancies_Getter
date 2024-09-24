from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file import JSONHandler
from pprint import pprint


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем.
    Запрашивает:
    - поисковый запрос,
    - кол-во (топ-N) вакансий по заработной плате для вывода,
    - ключевые слова в описании (для фильтрации),
    - диапазон зарплат для фильтрации.
    """

    # platforms: list[str] = ["HeadHunter"]

    # Поисковый запрос - далее используется как атрибут keyword
    # функции        get_vacancies_data(self, keyword: str, per_page: int, to_page: int)

    search_query: str = input("Введите поисковый запрос (например Python):   ")

    top_n: int = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words: list[str] = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()

    salary_range_dict: dict = get_salary_range_from_user()

    #
    # Получаем список вакансий с hh.
    hh_handler: HeadHunterAPI = HeadHunterAPI()
    if top_n * 5 <= 100:
        hh_handler.get_vacancies_data(search_query, top_n * 5, 1)
    else:
        hh_handler.get_vacancies_data(search_query, 100, 1)

    #
    # Преобразуем информацию с HH в список объектов Vacancy
    vac_obj_list: list[Vacancy] = Vacancy.cast_to___objects_list(hh_handler.vacancies)
    # pprint(vac_obj_list)
    print(f"\nС ресурса HeadHunter получено вакансий:   {len(vac_obj_list)}")

    #
    # Фильтрация объектов-вакансий по словам:
    filtered_vacancies: list[Vacancy] = filter_vacancies(vac_obj_list, filter_words)
    if len(filtered_vacancies) == 0:
        print("По указанным словам нет подходящих вакансий. Список остаётся не отфильтрован по ним.")
        filtered_vacancies = vac_obj_list
    else:
        print(f"После фильтрации по словам, их осталось:   {len(filtered_vacancies)}")

    #
    # Фильтрация объектов-вакансий по зарплате:
    ranged_vacancies: list[Vacancy] = get_vacancies_by_salary(filtered_vacancies, salary_range_dict)
    if len(ranged_vacancies) == 0:
        print("После фильтрации по зарплате, вакансий не осталось. Завершение программы.")
        return
    print(f"После фильтрации по зарплате, их осталось:   {len(ranged_vacancies)}")

    #
    # Сортировка объектов-вакансий по зарплате:     сначала с большей ЗП:
    # sorted_vacancies: list[Vacancy] = sort_vacancies(ranged_vacancies)
    sorted_vacancies: list[Vacancy] = sort_vacancies_by_magic_methods_inplace(ranged_vacancies)

    #
    # Взятие top-n объектов-вакансий:
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print("\nВыводим ТОП вакансий:")
    print_vacancies(top_vacancies)

    #
    # Сохранение информации о вакансиях в файл
    final_save_vacancies_to_file(top_vacancies)


def final_save_vacancies_to_file(vacancies_obj_list: list[Vacancy]) -> None:
    """
    Принимает список объектов-вакансий.
    Запрашивает у пользователя подтверждение на сохранение в файл.
    Производит сохранение вакансий в файл (без дублирования в файле).

    """
    while True:
        print(f"\nВакансий в 'топе': {len(vacancies_obj_list)}")
        user_answer: str = input(f"Сохраняем их в файл? (да/нет):   ")

        if user_answer.isalpha() and user_answer.lower() == "да":
            file_name: str = input("Укажите имя файла (можно не указывать, тогда используется имя по умолчанию):  ")

            if len(file_name):
                json_handler = JSONHandler(file_name)
            else:
                json_handler = JSONHandler()

            for vac_obj in vacancies_obj_list:
                json_handler.add_data_to_file(vac_obj)
            return

        elif user_answer.isalpha() and user_answer.lower() == "нет":
            print("Пропускаем запись в файл.")
            return

        else:
            print("\nТребуется повторное подтверждение.")

def print_vacancies(vacancies_obj_list: list[Vacancy]) -> None:
# def return_vacancies_for_print(vacancies_obj_list: list[Vacancy]) -> list[Vacancy]:
    """
    Принимает список объектов типа Vacancy,
    Выводит в консоль объекты-вакансии в виде:
    Разработчик Python.   https...   От 60000 руб.   Знание Python (средний уровень). Знание ООП...
    (добавляет пробелы, точки)
    """
    list_of_strings_for_delete: list[str] = ["<highlighttext>", "</highlighttext>"]

    for vac_obj in vacancies_obj_list:
        req_str: str = vac_obj.requirements

        # В из строки requirements удаляются строки из списка ["<highlighttext>", "</highlighttext>"]
        for str_for_del in list_of_strings_for_delete:
            req_str = req_str.replace(str_for_del, "")

        print(f"{vac_obj.speciality}.   {vac_obj.https_path}   {vac_obj.salary_str}.   {req_str}")



def get_top_vacancies(vacancies_obj_list: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Принимает список объектов типа Vacancy,
    Возвращает список объектов-вакансий, длиной равный значению top-n.
    """
    if top_n <= len(vacancies_obj_list):
        return vacancies_obj_list[0:top_n]
    else:
        return vacancies_obj_list


def sort_vacancies_by_magic_methods_inplace(vacancies_obj_list: list[Vacancy]) -> list[Vacancy]:
    """
    Принимает список объектов типа Vacancy,
    Возвращает отсортированный по зарплате (по убыванию) список объектов.
    """
    limit_index = len(vacancies_obj_list)

    while limit_index > 1:
        for i in range(1, limit_index):

            # Если по данному индексу (i) объект-вакансия имеет ЗП бОльшую, нежели по нижестоящему индексу (i - 1),
            if vacancies_obj_list[i - 1] < vacancies_obj_list[i]:

                # "дёргаем" объект-вакансию с бОльшей ЗП (по индексу i),
                vac_obj_poped: Vacancy = vacancies_obj_list.pop(i)
                # и помещаем по меньшему индексу (i - 1)
                vacancies_obj_list.insert(i - 1, vac_obj_poped)

        # По прошествию одного (первого) прохода, по индексу -1 окажется объект-вакансия с меньшей ЗП.
        # Эту вакансию уже в следующем проходе в счёт не берём.
        limit_index -= 1

    return vacancies_obj_list


# def sort_vacancies(vacancies_obj_list: list[Vacancy]) -> list[Vacancy]:
#     """
#     Принимает список объектов типа Vacancy,
#     Возвращает отсортированный по зарплате (по убыванию) список объектов.
#     """
#     vacancies_initial_length: int = len(vacancies_obj_list)
#     sorted_obj_list: list[Vacancy] = []
#
#     while len(sorted_obj_list) != vacancies_initial_length:
#
#         # Макс.зп., которую удалось найти в списке объектов.
#         max_found_salary: int = 0
#         # Индекс объекта с макс.зп.
#         max_salary_obj_index: int = 0
#
#         # Последовательное "выдёргивание" объектов с бОльшей ЗП, до тех пор,
#         # пока длина сортированного списка не станет равна длине изначального списка объектов.
#         for i, vac_obj in enumerate(vacancies_obj_list):
#             if vac_obj.salary_dict["from"] > max_found_salary:
#                 max_found_salary = vac_obj.salary_dict["from"]
#                 max_salary_obj_index = i
#             if vac_obj.salary_dict["to"] > max_found_salary:
#                 max_found_salary = vac_obj.salary_dict["to"]
#                 max_salary_obj_index = i
#
#         sorted_obj_list.append(vacancies_obj_list.pop(max_salary_obj_index))
#     return sorted_obj_list


def get_vacancies_by_salary(vacancies_obj_list: list[Vacancy], salary_dict: dict[str, int | str]) -> list[Vacancy]:
    """
    Принимает список объектов типа Vacancy, словарь с диапазоном зарплаты.
    Возвращает список объектов, у которых зарплата "пересекается" с указанным диапазоном.
    """
    filtered_vacancies: list[Vacancy] = []
    for vac_obj in vacancies_obj_list:
        if salary_dict["from"] <= vac_obj.salary_dict["from"] <= salary_dict["to"]:
            filtered_vacancies.append(vac_obj)
            continue
        if salary_dict["from"] <= vac_obj.salary_dict["to"] <= salary_dict["to"]:
            filtered_vacancies.append(vac_obj)

    return filtered_vacancies


def filter_vacancies(vacancies_obj_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """
    Принимает список объектов типа Vacancy, список слов - для фильтрации списка объектов.
    Возвращает список объектов, в описании которых есть данные слова.
    """
    filtered_vacancies: list[Vacancy] = []
    for vac_obj in vacancies_obj_list:
        for word in filter_words:
            if word in vac_obj.speciality or word in vac_obj.requirements:
                filtered_vacancies.append(vac_obj)
                break

    return filtered_vacancies



def get_salary_range_from_user(currency: str = "RUR", is_in_test: bool = False) -> dict[str, int | str]:
    """
    Запрашивает у пользователя диапазон зарплат,
    Проверяет корректность диапазона.
    Возвращает словарь вида:     {"from": 50000, "to": 90000, "currency": "RUR"}
    """
    if is_in_test:
        return {"from": 50000, "to": 90000, "currency": "RUR"}

    print("Ввод диапазона зарплат.")

    while True:

        salary_from_input: str = ""
        while not salary_from_input.isdigit():
            salary_from_input = input("ЗП от (введите без доп.символов):   ")
            if not salary_from_input.isdigit():
                print("Ваш ввод не является числовым. Повторите ввод.")

        salary_from: int = int(salary_from_input)

        salary_to_input: str = ""
        while not salary_to_input.isdigit() or int(salary_to_input) < salary_from:
            salary_to_input = input(f"ЗП до (не менее {salary_from}):   ")
            if not salary_to_input.isdigit():
                print("Ваш ввод не является числовым. Повторите ввод.")
            elif int(salary_to_input) < salary_from:
                print("Верхняя граница зарплаты не может быть меньше нижней границы. Повторите ввод.")

        salary_to: int = int(salary_to_input)

        while True:
            print(f"\nВы указали диапазон зарплат: {salary_from} - {salary_to} {currency}")
            user_answer: str = input(f"Продолжаем с ним? (да/нет):   ")

            if user_answer.isalpha() and user_answer.lower() == "да":
                return {"from": salary_from, "to": salary_to, "currency": currency}

            if user_answer.isalpha() and user_answer.lower() == "нет":
                print("\nДавайте повторим ввод.")
                break


# if __name__ == "__main__":
#     vac_1 = Vacancy("sp1", "req1", "s1", {"from": 1, "to": 10, "currency": "RUR"}, "https1")
#     vac_2 = Vacancy("sp2", "req2", "s2", {"from": 2, "to": 20, "currency": "RUR"}, "https2")
#
#     final_save_vacancies_to_file([vac_1, vac_2])
    # range_dict: dict = get_salary_range_from_user()

    # Получаем список вакансий с hh.
    # hh_handler: HeadHunterAPI = HeadHunterAPI()
    # hh_handler.get_vacancies_data("Python", 40, 1)
    # pprint(hh_handler.vacancies)

    # vac_obj_list: list[Vacancy] = Vacancy.cast_to___objects_list(hh_handler.vacancies)
    # pprint(vac_obj_list)

    # for vac in vac_obj_list:
    #     print(vac.speciality, vac.https_path, vac.salary_str, vac.requirements)
