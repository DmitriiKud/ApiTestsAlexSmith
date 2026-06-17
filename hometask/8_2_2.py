import requests

url = "https://reqres.in/api/register"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_post = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(url, json=json_post, headers=headers)

print(response.status_code)
print(response.text)
token = response.json().get("token")
print(len(token))