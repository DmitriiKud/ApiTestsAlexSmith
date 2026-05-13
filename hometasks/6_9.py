import requests

# Здесь я сначала создал кортежик с 5ю новыми локациями, которые буду добавлять на сервер
json_create_location = (
    {
        "location": {"lat": -38.383494, "lng": 33.427362},
        "accuracy": 50,
        "name": "Frontline house - HQ",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park", "shop"],
        "website": "http://google.com",
        "language": "French-IN"
    },
    {
        "location": {"lat": -38.383494, "lng": 33.427363},
        "accuracy": 50,
        "name": "Backline outlet",
        "phone_number": "(+91) 982 123 4567",
        "address": "45, main road, cohen 12",
        "types": ["shoe store", "outlet"],
        "website": "http://google.com",
        "language": "French-IN"
    },
    {
        "location": {"lat": -38.383495, "lng": 33.427360},
        "accuracy": 50,
        "name": "Urban footwear",
        "phone_number": "(+91) 981 555 8888",
        "address": "12, lake view, cohen 03",
        "types": ["sports shoes", "retail"],
        "website": "http://google.com",
        "language": "French-IN"
    },
    {
        "location": {"lat": -38.383493, "lng": 33.427365},
        "accuracy": 50,
        "name": "Vintage sole",
        "phone_number": "(+91) 984 000 1122",
        "address": "7, heritage lane, cohen 22",
        "types": ["leather shoes", "boutique"],
        "website": "http://google.com",
        "language": "French-IN"
    },
    {
        "location": {"lat": -38.383496, "lng": 33.427358},
        "accuracy": 50,
        "name": "Comfort walk",
        "phone_number": "(+91) 987 654 3210",
        "address": "90, park street, cohen 08",
        "types": ["orthopedic shoes", "walking store"],
        "website": "http://google.com",
        "language": "French-IN"
    },
)

# решил упороться и создать декораторы на запись и чтение файла
def write_place_id_to_file(func):
    """Декоратор для сохранения id в файл."""

    def wrapper(self, location):
        func(self, location)

        # Получаем id из атрибута, который будет в декорируемом методе
        if hasattr(self, 'place_id'):
            with open("place_id3.txt", "a") as file:  # "a" это append
                file.write(f"{self.place_id}\n")
            print("Following ID is written to file " + self.place_id)

    return wrapper

def read_place_id_from_file(func):
    """Декоратор для чтения id из файла."""

    def wrapper(self):

        # Получаем id из файла через контекстный файловый менеджер
        with open("place_id3.txt", "r") as file:  # "r" это' read
            place_id_list = file.read().splitlines()
            self.place_id_list = place_id_list

        return func(self)

    return wrapper


# Это собственно тестовый класс
class TestNewLocation():
    """Работа с новой локацией."""
    base_url = "https://rahulshettyacademy.com"  # базовая url
    key = "?key=qaclick123"  # параметр для всех запросов
    post_resource = "/maps/api/place/add/json"  # ресурс метода post

    @write_place_id_to_file
    def create_new_location(self, location):
        """Метод для создания новой локации."""

        post_url = self.base_url + self.post_resource + self.key
        print("Create location in " + post_url)
        result_post = requests.post(post_url, json=location)
        print("Location is created " + result_post.text)
        self.place_id = result_post.json()["place_id"]

    @read_place_id_from_file
    def save_place_id_list_from_file(self):
        """Метод для сохранения всех place_id из файла"""
        return self.place_id_list

    # ну это мы уже тестируем наличие созданных локаций по переданному списку place_id из файла
    def test_create_new_location(self, place_id_list):

        for place_id in place_id_list:
            get_resource = "/maps/api/place/get/json"  # ресурс метода get
            get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id

            result_get = requests.get(get_url)
            print(result_get.text)
            print("Status code : " + str(result_get.status_code))
            assert 200 == result_get.status_code, "Fail!!! Wrong request"
            print("Success!!! New location is saved")


new_place = TestNewLocation()

# в этих строчках я создавал новые локации. Закомментировал их, так как это было разовое действие
# for location in json_create_location:
#     new_place.create_new_location(location)

# здесь я вызвал методм и сохранил в список все place_id из файла
place_id_list = new_place.save_place_id_list_from_file()

# вот запуск теста
new_place.test_create_new_location(place_id_list)
