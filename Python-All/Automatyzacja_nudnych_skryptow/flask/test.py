import requests

BASE = "http://127.0.0.1:8822"

try:
    response = requests.get(BASE + "/helloworld")
except ConnectionError as e:
    print(e)

print(response.json())
