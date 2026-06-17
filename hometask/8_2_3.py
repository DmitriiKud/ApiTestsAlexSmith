import requests

url = "https://petstore.swagger.io/v2/user/createWithArray"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_post = [
  {
    "id": 1,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

response = requests.post(url, json=json_post, headers=headers)

print(response.status_code)
print(response.text)