import requests

"""
Я решил выводить на печать категорию, статус код и саму шутку.

"""

class TestJokes:
    """Создание новой шутки"""

    def __init__(self):
        pass

    def get_categories(self):
        """Получение категорий"""
        url = "https://api.chucknorris.io/jokes/categories"
        result = requests.get(url)
        category_list = result.json()
        return category_list

    def test_get_category_joke(self, category):
        """Создание шутки для категории"""
        url = "https://api.chucknorris.io/jokes/random?category=" + category

        result = requests.get(url)
        print("статус код : " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        print("Успешно!!! Мы получили новую шутку")
        # result.encoding = 'utf-8'
        joke = result.json()
        print(joke.get("value"))


joke = TestJokes()
categories = joke.get_categories()
category = str(input("Введите название категории: "))

"""Здесь цикл, чтобы пользователь сразу ввел категорию еще раз"""

while True:
    if category in categories:
        print("Спасибо за выбор категории " + category)
        joke.test_get_category_joke(category)
        break
    else:
        category = str(input("Вы выбрали несуществующую категорию, введите еще раз : "))