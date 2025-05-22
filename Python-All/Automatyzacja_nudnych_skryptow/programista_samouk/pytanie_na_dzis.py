import datetime

questions = ""

questions = input(
    "Jakie jest Twoje pytanie na dziś? Nie o Tobie, ale o sprawach związanych z życiem?"
    + "\n"
)

now = datetime.datetime.now()

now_in_str = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

with open(
    "/home/mateusz/Dokumenty/Dokumenty/Telefon/pytanie.txt", "a", encoding="utf-8"
) as file_one:
    file_one.write(now_in_str + "\n" + questions + "\n")

with open("/home/mateusz/Dokumenty/Dokumenty/Telefon/pytanie.txt", "r") as file_one:
    print(file_one.read())
