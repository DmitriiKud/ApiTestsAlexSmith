import json

import requests


url = "https://catfact.ninja/fact?max_length=100"

response = requests.get(url)

fields = json.loads(response.text)
print(list(fields))
