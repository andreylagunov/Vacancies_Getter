from src.vacancy import Vacancy
from pytest import fixture

@fixture
def get_vacancy_obj():
    return Vacancy("C++", "cmake", "От 50000 до 200000 руб", {"from": 50000, "to": 200000, "currency": "RUR"}, "www")

@fixture
def get_vacancy_obj_2():
    return Vacancy("Python", "PyCharm", "От 40000 до 200000 руб", {"from": 40000, "to": 200000, "currency": "RUR"}, "www")

@fixture
def get_vacancy_obj___with_faulty_speciality():
    return Vacancy(333, "cmake", "От 50000 до 200000 руб", {"from": 50000, "to": 200000, "currency": "RUR"}, "www")

@fixture
def get_vacancies_dicts__in_list():
    vacancies = [
        {'id': '107300510', 'premium': False, 'name': 'Аналитик данных (Data Analyst) г. Ташкент', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '2759', 'name': 'Ташкент', 'url': 'https://api.hh.ru/areas/2759'}, 'salary': None,
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-09-16T09:06:52+0300', 'created_at': '2024-09-16T09:06:52+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=107300510',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/107300510?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/107300510',
         'relations': [], 'employer': {'id': '3807759', 'name': 'CLICK', 'url': 'https://api.hh.ru/employers/3807759',
                                       'alternate_url': 'https://hh.ru/employer/3807759',
                                       'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/6862050.png',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/1310448.png',
                                                     '240': 'https://img.hhcdn.ru/employer-logo/6862051.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3807759',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'SQL для сложных и производительных запросов (CTE, оконные функции). <highlighttext>Python</highlighttext> для анализа данных (pandas, numpy). Опыт работы с инструментами бизнес...',
            'responsibility': 'Исследование и анализ источников данных (внутренних и внешних). Управление требованиями к пользовательским витринам данных (сбор, анализ, актуализация). Разработка и оптимизация...'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '156', 'name': 'BI-аналитик, аналитик данных'}],
         'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None},
        {'id': '106109534', 'premium': False, 'name': 'Бэкенд-разработчик Python Django', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 80000, 'to': 120000, 'currency': 'RUR', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-08-21T11:41:03+0300', 'created_at': '2024-08-21T11:41:03+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106109534',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/106109534?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/106109534',
         'relations': [],
         'employer': {'id': '11359650', 'name': 'Сапплай Директор', 'url': 'https://api.hh.ru/employers/11359650',
                      'alternate_url': 'https://hh.ru/employer/11359650',
                      'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6901559.png',
                                    'original': 'https://img.hhcdn.ru/employer-logo-original/1320377.png',
                                    '90': 'https://img.hhcdn.ru/employer-logo/6901558.png'},
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11359650',
                      'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Опыт работы с Django Framework, Rest Framework и базами данных (PostgreSQL). Умение разбираться в чужом коде. Быть в состоянии выдержать...',
            'responsibility': 'Разработка бэкенда для веб-приложения на <highlighttext>Python</highlighttext> Django. Выполнять таски в срок. Быть на связи в рабочее время. '},
         'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
         'working_time_intervals': [
             {'id': 'from_four_to_six_hours_in_a_day', 'name': 'Можно сменами по\xa04-6\xa0часов в\xa0день'}],
         'working_time_modes': [{'id': 'start_after_sixteen', 'name': 'С\xa0началом дня после 16:00'}],
         'accept_temporary': True, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
         'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'part', 'name': 'Частичная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None},
        {'id': '107057173', 'premium': False, 'name': 'Младший программист', 'department': None, 'has_test': False,
         'response_letter_required': False,
         'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': None,
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-09-10T13:53:45+0300', 'created_at': '2024-09-10T13:53:45+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=107057173',
         'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/107057173?host=hh.ru',
         'alternate_url': 'https://hh.ru/vacancy/107057173', 'relations': [],
         'employer': {'id': '11423828', 'name': 'STC', 'url': 'https://api.hh.ru/employers/11423828',
                      'alternate_url': 'https://hh.ru/employer/11423828', 'logo_urls': None,
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11423828',
                      'accredited_it_employer': False, 'trusted': False}, 'snippet': {
            'requirement': 'Базовое знания любого языка программирования. Алгоритмическая/ Математическая база. Базовое знание университетской физики будет плюсом.',
            'responsibility': 'Разработка высоко нагруженных микросервисов для системы электронного документооборота. Реализация серверной бизнес логики. Юнит/функциональные тесты. Работа с тех. '},
         'contacts': None, 'schedule': {'id': 'flexible', 'name': 'Гибкий график'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None},
        {'id': '107347408', 'premium': False, 'name': 'Junior Python', 'department': None, 'has_test': False,
         'response_letter_required': False,
         'area': {'id': '1002', 'name': 'Минск', 'url': 'https://api.hh.ru/areas/1002'}, 'salary': None,
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-09-16T16:53:28+0300', 'created_at': '2024-09-16T16:53:28+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=107347408',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/107347408?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/107347408',
         'relations': [], 'employer': {'id': '115911', 'name': 'Энтерра', 'url': 'https://api.hh.ru/employers/115911',
                                       'alternate_url': 'https://hh.ru/employer/115911',
                                       'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6059794.png',
                                                     '90': 'https://img.hhcdn.ru/employer-logo/6059793.png',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/1109798.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=115911',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Опыт программирования от 0,5 года с <highlighttext>Python</highlighttext> и\\или JS. Опыт работы с каким-то из инструментов Jmeter/gatling...',
            'responsibility': 'Умение анализировать проблемы производительности по результатам НТ, заведение дефектов, составление рекомендаций, участие в работах по оптимизации производительности.'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None},
        {'id': '107368643', 'premium': False, 'name': 'Back-end разработчик', 'department': None, 'has_test': False,
         'response_letter_required': False, 'area': {'id': '72', 'name': 'Пермь', 'url': 'https://api.hh.ru/areas/72'},
         'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
         'address': {'city': 'Пермь', 'street': 'улица Вагановых', 'building': '11А', 'lat': 58.023226,
                     'lng': 56.280387, 'description': None, 'raw': 'Пермь, улица Вагановых, 11А', 'metro': None,
                     'metro_stations': [], 'id': '4524931'}, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-09-17T09:15:32+0300', 'created_at': '2024-09-17T09:15:32+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=107368643',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/107368643?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/107368643',
         'relations': [], 'employer': {'id': '3919922', 'name': 'It-M', 'url': 'https://api.hh.ru/employers/3919922',
                                       'alternate_url': 'https://hh.ru/employer/3919922',
                                       'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/3392573.png',
                                                     '240': 'https://img.hhcdn.ru/employer-logo/3392574.png',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/737899.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3919922',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Знание в области информационных технологий или аналогичной области. Знание <highlighttext>Python</highlighttext> (и Django), PostgreSQL. Опыт работы с реляционными базами данных, включая...',
            'responsibility': 'Способность эффективно общаться с другими членами команды и передавать техническую информацию.'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}
    ]
    return vacancies
