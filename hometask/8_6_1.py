import requests

url = "https://reqres.in/api/users/3"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]

response = requests.put(url, json=json_put, headers=headers)
print(response.status_code)
print(response.json())
