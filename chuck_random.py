import requests


class TestNewJoke:
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_get_new_joke(self):
        """Создание случайной шутки"""
        url = "https://api.chucknorris.io/jokes/random"
        print(url)

        result = requests.get(url)
        print("статус код : " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        print("Успешно!!! Мы получили новую шутку")
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_categories = check.get("categories")
        print(check_categories)
        assert check_categories == []
        print("Категория верна")

        check_value = check.get("value")
        print(check_value)
        name = "Chuck"
        assert name in check_value, "Chuck отсутствует"
        print("Chuck присутствует")

    def test_get_new_joke_category(self):
        """Создание случайной шутки из опредленной категории"""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)

        result = requests.get(url)
        print("статус код : " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        print("Успешно!!! Мы получили новую шутку")
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_categories = check.get("categories")
        print(check_categories)
        assert check_categories == ["sport"]
        print("Категория верна")

        check_value = check.get("value")
        print(check_value)
        name = "Chuck"
        assert name in check_value, "Chuck отсутствует"
        print("Chuck присутствует")

    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему."""
        category = "spor"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)

        result = requests.get(url)
        print("статус код : " + str(result.status_code))
        assert 404 == result.status_code, "Провал!!! Запрос ошибочный"
        print("Успешно!!! Мы получили новую шутку")
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верна")
        #
        # check_value = check.get("value")
        # print(check_value)
        # name = "Chuck"
        # assert name in check_value, "Chuck отсутствует"
        # print("Chuck присутствует")


joke = TestNewJoke()
joke.test_create_new_random_categories_joke()

