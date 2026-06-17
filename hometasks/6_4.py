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
for category in joke.get_categories():
    print("Эта шутка из категории : " + category)
    joke.test_get_category_joke(category)
    print()