import requests


courses = ["Python-разработчик с нуля", "Java-разработчик с нуля",
           "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
        "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
        "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
        "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
        "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]
max = max(durations)
min = min(durations)


def get_uniq_names(mentors=mentors):
    new_lst_set = set(sum(mentors, []))
    new_list = ", ".join(new_lst_set).split()
    unique_names = sorted(set(new_list[0::2]))
    return unique_names


def get_popular_name(mentors=mentors):
    new_lst_set = sum(mentors, [])
    new_list = ", ".join(new_lst_set).split()
    unique_names = sorted(new_list[0::2])
    popular = []
    for name in unique_names:
        popular.append((name, unique_names.count(name)))
    popular = list(set(popular))
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0:3]
    top_str = []
    for name, count in top_3:
        top_str.append(name + ': ' + str(count))
        return top_str


def get_course_duration(courses=courses, mentors=mentors, durations=durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {
            'title': course,
            'mentors': mentor,
            'duration': duration}
        courses_list.append(course_dict)

    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if duration == max:
            maxes.append(index)
        elif duration == min:
            minis.append(index)

    courses_max = []
    for id in maxes:
        courses_max.append(courses_list[id]['title'])

    return f'Самый длинный курс(ы): {", ".join(courses_max)} - {max} месяца(ев)'


def add_folder_yandex(token_yandex: str, name_of_folder: str):
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(url_folder, headers ={'Authorization': 'OAuth {}'.format(token_yandex)}, params = {'path' : name_of_folder})
    return response.status_code


def check_folder_yandex(token_yandex: str, name_of_folder: str):
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.get(url_folder, headers ={'Authorization': 'OAuth {}'.format(token_yandex)}, params = {'path' : name_of_folder})
    return response.status_code
