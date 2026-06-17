import requests

url = "https://reqres.in/api/login"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

json_post = [
    {
        "email": "peter@klaven"
    }
]

response = requests.post(url, json=json_post, headers=headers)

print(response.status_code)
print(response.text)