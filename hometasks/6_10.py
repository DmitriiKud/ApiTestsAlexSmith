import requests

# опять реализовал декораторы на запись в новый файл place_id4.txt и чтение из старого файла place_id3.txt
def read_place_id_from_file(func):
    """Декоратор для чтения id из файла place_id3.txt."""

    def wrapper(self):

        # Получаем id из файла через контекстный файловый менеджер
        with open("place_id3.txt", "r") as file:
            place_id_list = file.read().splitlines()
            self.place_id_list = place_id_list

        return func(self)

    return wrapper

def write_place_id_to_new_file(func):
    """Декоратор для сохранения id в новый файл place_id4.txt."""
    def wrapper(self, place_id_list):
        result_list = func(self, place_id_list) # тут я сохраняю переданный из теста список оставшихся локаций

        with open("place_id4.txt", "w") as file:
            for place_id in result_list:
                file.write(f"{place_id}\n")
        print(f"Following {len(result_list)} ID(s) are written to file place_id4.txt: {result_list}")
        return result_list # возвращаю этот список в декораторе только для того, чтобы последней строчкой вывести его в консоль

    return wrapper

# Это собственно тестовый класс
class TestNewLocation():
    """Работа с новой локацией."""
    base_url = "https://rahulshettyacademy.com"  # базовая url
    key = "?key=qaclick123"  # параметр для всех запросов
    post_resource = "/maps/api/place/add/json"  # ресурс метода post

    def delete_location(self, place_ids_to_delete):
        """Метод удаляющий локации из переданного списка place_id."""
        for place_id in place_ids_to_delete:
            delete_resource = "/maps/api/place/delete/json"  # ресурс метода delete
            delete_url = self.base_url + delete_resource + self.key

            json_delete_location = {
                "place_id": place_id,
            }

            result_delete = requests.delete(delete_url, json=json_delete_location)
            print(result_delete.text)
            print("Status code : " + str(result_delete.status_code))
            assert 200 == result_delete.status_code, "Fail!!! Wrong request"
            print(f"Success!!! The location {place_id} is deleted")

    # метод get, которым мы подтверждаем, что оставшиеся 3 локации существуют я реализовал как тест
    @write_place_id_to_new_file
    def test_location_exist(self, place_id_list):
        """Тест проверки существования локации на сервере + добавление в список."""
        confirmed_place_list = []
        for place_id in place_id_list:
            get_resource = "/maps/api/place/get/json"  # ресурс метода get
            get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
            result_get = requests.get(get_url)

            if result_get.status_code == 200:
                confirmed_place_list.append(place_id)
                print(f"Location {place_id} exists and added to the list")
            else:
                print(f"Location {place_id} does not exist (status {result_get.status_code})")

        print(f"Существующие локации: {confirmed_place_list}")
        return confirmed_place_list

    @read_place_id_from_file
    def save_place_id_list_from_file(self):
        """Метод для сохранения всех place_id из файла."""
        return self.place_id_list


new_place = TestNewLocation()

# здесь я вызвал метод и сохранил в список все place_id из файла place_id4.txt
place_id_list = new_place.save_place_id_list_from_file()

# тут я сохранил 2 и 4 place_id, которые передам в метод удаления
place_ids_to_delete = [place_id_list[1], place_id_list[3]]

# вызов метода для удаления 2 и 4 place_id
new_place.delete_location(place_ids_to_delete)

# вызов теста, который подтверждает, что 3 локации из 5 остались и срабатывает декоратор, который записывает в новый файл
existing_places  = new_place.test_location_exist(place_id_list)

print(f"Финальный результат - существующие локации: {existing_places}")
