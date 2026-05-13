"""
{ "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
 }
"""
import requests

# Давайте изменим поле address
new_address = "100 Lenina street, RU"
place_id = "c104d917f4b60e2c9a5feda6c9cbf279"
base_url = 'https://rahulshettyacademy.com'    # базовая url
key = '?key=qaclick123'                  # ключ допуска
put_resourse = '/maps/api/place/update/json'   # путь метода put

put_url = base_url + put_resourse + key
print(put_url)

json_put_location = {                          # тело запроса put
            "place_id": place_id,               # переменная с place_id

            "address": new_address,             # переменная с новым адрессом

            "key":"qaclick123"
        }

result_put = requests.put(put_url, json=json_put_location)     # отпрвака запроса put, который включает url и тело запроса
print(result_put.json())

print(f'Статус-код: {result_put.status_code}')
assert result_put.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код PUT корректен')

check_response_put = result_put.json()

msg = check_response_put.get("msg")    # получение значения обязательного поля ответа
print(msg)
assert msg == 'Address successfully updated', 'ОШИБКА, Поле MSG некорректно'
print('Поле MSG корректно')

# Нам понадобится вновь отправить метод Get, и убедиться, что поле изменилось.
get_resource = "/maps/api/place/get/json"  # ресурс метода post
get_url = base_url + get_resource + key + "&place_id=" + place_id
result_get = requests.get(get_url)
print(result_get.json())

check_response_get = result_get.json()

print(f'Статус-код: {result_get.status_code}')
assert result_get.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код GET корректен')

actual_address = check_response_get.get('address')    # актуальный (фактический) адрес локации
print(actual_address)
assert actual_address == new_address, 'ОШИБКА, Адрес не изменился'
print('Адрес изменился')