import requests

url = "https://reqres.in/api/login"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_post = [
    {
        "username": "1",
        "email": "1@mail.ru",
        "password": "qwer1234"
    }
]

response = requests.post(url, json=json_post, headers=headers)

print(response.status_code)
print(response.text)