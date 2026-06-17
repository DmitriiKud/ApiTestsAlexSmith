import requests

url = "https://reqres.in/api/users?page=2"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
my_dict = response.json()
# данный генератор берет самый первый ключ значение которого удовлетворяет условию
key = next((k for k, v in my_dict.items() if v == 6), None)
print(key)