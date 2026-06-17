import requests
from pyexpat.errors import messages

url = "https://dog.ceo/api/breeds/image/random/100"

headers = {
    "x-api-key": "free_user_3DU3H2bw6CtsSnSoYA8Ncx2XzzQ"
}

response = requests.get(url, headers=headers)
message = response.json().get("message")
print(len(message))
