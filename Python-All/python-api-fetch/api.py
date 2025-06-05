"""The module provides methods for getting information with API."""
import requests

response = requests.get("https://randomuser.me/api", timeout=10)
print(
    response.status_code
)  # If it returns 200. That means our app is connected successfully
print(response.json())  # This will return the json data.

gender = response.json()["results"][0]["gender"]  # It will return male or female.
print(gender)

title = response.json()["results"][0]["name"]["title"]  # It will return the title.

first_name = response.json()["results"][0]["name"][
    "first"
]  # It will return the first name.

last_name = response.json()["results"][0]["name"][
    "last"
]  # It will return the first name.

age = response.json()["results"][0]["dob"]["age"]

print(f"{title}. {first_name} {last_name}")
print(f"Age: {age}.")
