import json

from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:
    """Класс содержащий тесты по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET
        Checking.check_status_code(result_post, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)  # проверка методом GET
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # проверка методом GET
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')


        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # проверка методом GET
        Checking.check_status_code(result_get, 404)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', "failed")