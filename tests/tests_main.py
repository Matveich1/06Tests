from unittest import TestCase
from main import get_uniq_names, get_popular_name, get_course_duration, add_folder_yandex, check_folder_yandex


class Test_data_collection(TestCase):
    def setUp(self) -> None:
        self.courses = ["Python-разработчик с нуля", "Java-разработчик с нуля",
                        "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

        self.mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
             "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]

        self.durations = [14, 20, 12, 20]
        self.max = max(self.durations)
        self.min = min(self.durations)
        return super().setUp()

    def test_get_uniq_names(self):
        result = get_uniq_names(self.mentors)
        excepted = ['Адилет', 'Азамат', 'Александр', 'Алексей', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', 'Евгений', 'Елена', 'Иван',
                    'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', 'Сергей', 'Татьяна', 'Тимур', 'Филипп', 'Эдгар', 'Юрий']
        self.assertEqual(result, excepted)

    def test_get_popular_name(self):
        result = get_popular_name(self.mentors)
        excepted = ['Александр: 10']
        self.assertEqual(result, excepted)

    def test_get_course_duration(self):
        result = get_course_duration(
            self.courses, self.mentors, self.durations)
        expected = 'Самый длинный курс(ы): Java-разработчик с нуля, Frontend-разработчик с нуля - 20 месяца(ев)'
        self.assertEqual(result, expected)


token = ''
name_folder = 'Home Work Tests'


class Test_yandex_disk (TestCase):
    def setUp(self) -> None:
        self.token = token
        self.folder = name_folder
        return super().setUp()

    def test_add_folder(self):
        result = add_folder_yandex(self.token, self.folder)
        expected = 201
        self.assertEqual(result, expected)

    def test_check_folder(self):
        result = check_folder_yandex(self.token, self.folder)
        expected = 200
        self.assertEqual(result, expected)

    def test_add_folder_if_exsists(self):
        result = add_folder_yandex(self.token, self.folder)
        self.assertEqual(result, 409)
