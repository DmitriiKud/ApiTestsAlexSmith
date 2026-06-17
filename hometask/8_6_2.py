import requests

url = "https://petstore.swagger.io/v2/store/order/1"


response = requests.delete(url)
print(response.status_code)
print(response.json())
