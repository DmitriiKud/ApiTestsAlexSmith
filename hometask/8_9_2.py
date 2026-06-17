import requests

url = "https://dog.ceo/api/breed/hound/images"

response = requests.get(url)
message = response.json().get("message")
count = 0
for i in message:
    count += 1 if "hound-english" in i else 0

print(count)
