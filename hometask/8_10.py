"""
Проверить работспособонсть, так как были проблемы с сервисом.
"""

import requests

url_1 = "https://swapi.info/api/people/4/"
url_2 = "https://swapi.info/api/people"

def check_actor_played_with_weider(weiders_list, actors_list):
    return bool(set(weiders_list) & set(actors_list))

def write_actors_to_file(actors_list):
    with open("actors.txt", "w") as file:
        for actor in actors_list:
            file.write(f"{actor}\n")
        print(f"Актеры записаны. Всего их: {len(actors_list)}")

# Получаем фильмы Дарта Вейдера
response_weider = requests.get(url_1, verify=False)
films_list = response_weider.json().get("films")
print("Фильмы Вейдера:",films_list)

# Получаем всех актеров
response_people = requests.get(url_2, verify=False)
print(f"Все актеры: {response_people.json()}")

# сохраняем список актеров, игравших с Вейдором, используя функцию check_actor_played_with_weider
people_list = []
for i in response_people.json():
    actors_list = i.get("films")
    people_list.append(i["name"]) if check_actor_played_with_weider(films_list, actors_list) else None

print(f"Актеры, снимавшиеся с Вейдером: {set(people_list)}")
print(f"Количество актеров, снимавшихся с Вейдером: {len(set(people_list))}")

# записываем перечень уникальных имен актеров в файл
write_actors_to_file(list(set(people_list)))

