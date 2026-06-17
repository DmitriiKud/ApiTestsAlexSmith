import requests

url = "https://petstore.swagger.io/v2/pet"

json_put = [
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Bobik"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": "1",
                "name": "Bob"
            }
        ],
        "status": "available"
    }
]

response = requests.put(url, json=json_put)
print(response.status_code)
print(response.text)
