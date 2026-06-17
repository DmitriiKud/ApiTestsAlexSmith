import json

import requests


url = "https://catfact.ninja/facts?max_length=100&limit=5"

response = requests.get(url)

fields = json.loads(response.text)
print(list(fields))
