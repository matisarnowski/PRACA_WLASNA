imie = "Mateusz"
wiek = 30
wiek = str(wiek)
print(
    "{0} miał {1} lat, gdy napisał swój pierwszy program w Pythonie.".format(imie, wiek)
)
print(
    "{} miał {} lat, gdy napisał swój pierwszy program w Pythonie.".format(imie, wiek)
)
print(
    "{imie} miał {wiek} lat, gdy napisał swój pierwszy program w Pythonie.".format(
        imie="Mateusz", wiek=30
    )
)
print(imie + " miał " + wiek + " lat, gdy napisał swój pierwszy program w Pythonie.")
