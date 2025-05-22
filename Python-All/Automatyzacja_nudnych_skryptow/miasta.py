#!/usr/bin/python3

miasta = {
    "Toruń": (52.9823108, 18.5720631),
    "Brodnica": (53.24832, 19.40721),
    "Gliwice": (50.2931514, 18.72489),
    "Warszawa": (52.2319237, 21.0067265),
    "Gdańsk": (54.347629, 18.6452324),
    "Węgorzewo": (54.2138162, 21.7416569),
    "Kielce": (50.8717388, 20.6308626),
    "Chęciny": (50.8000835, 20.4622228),
}

wsp = miasta
print(miasta)

for i in miasta:
    print(i, wsp[i])
