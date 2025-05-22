"""Module providing a function to communicate with API."""
import requests

FROM_CURRENCY = str(input("Wprowadź walutę, którą chcesz przekonwertować: ")).upper()

TO_CURRENCY = str(input("Wprowadź walutę, na którą chcesz przekonwertować: ")).upper()

AMOUNT = float(input("Wprowadź ilość waluty, którą chcesz przekonwertować: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={AMOUNT}&from={FROM_CURRENCY}&to={TO_CURRENCY}",
    timeout=10,
)
print(response.status_code)
print(f"{AMOUNT} {FROM_CURRENCY} to {round(response.json()["rates"][TO_CURRENCY], 2)} {TO_CURRENCY}.")
