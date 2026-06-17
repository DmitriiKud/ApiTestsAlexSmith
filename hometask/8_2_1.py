import requests

url = "https://reqres.in/api/users"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_post = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url, headers=headers, json=json_post)

print(response.status_code)
print(response.text)
print(type(response.json().get("id")))
year = response.json().get("createdAt")[0:4]
print(year)