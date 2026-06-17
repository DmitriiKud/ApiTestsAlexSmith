import requests

url = "https://reqres.in/api/users/2"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)