import json


class Checking:

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает. ФР - ' + str(result.status_code)
        print(f"Успешно! Статус код = {result.status_code}")



    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает. ФР - ' + str(list(fields))
        print(list(fields))
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'ОШИБКА, Значение поля не совпадает. ФР - ' + str(check_info)
        print(check_info)
        print(f"Поле {field_name} верно!")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info, 'ОШИБКА, Данного слова нет в значении поля. ФР - ' + str(check_info)
        print(f"Слово {search_word} присутствует в значении поля {field_name}")