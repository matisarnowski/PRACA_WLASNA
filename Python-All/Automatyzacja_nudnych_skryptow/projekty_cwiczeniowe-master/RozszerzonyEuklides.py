#! /usr/local/bin/python3

while True:
    try:
        a = int(
            input(
                "Podaj pierwszą liczbę całkowitą dla, której wykonamy rozszerzony algorytm Euklidesa: "
            )
        )
        b = int(
            input(
                "Podaj drugą liczbę całkowitą, która będzie dzielnikiem w rozszerzonym algorytmie Euklidesa."
            )
        )
    except Exception as e:
        print(f"{e}")
        print("Podałeś nie to, co trzeba. ")
    if a < 1 or b < 1:
        print("Podaj jako wartości liczby całkowite większe od 1: ")
    else:
        break

a0 = a
b0 = b

p = 1
q = 0
r = 0
s = 1
c = new_r = new_p = 0

while b != 0:
    c = a % b
    quot = a // b
    a = b
    b = c
    new_r = p - quot * r
    new_s = q - quot * s
    p = r
    q = s
    r = new_r
    s = new_s

if p < 0 or q < 0:
    print(f"NWD({a0},{b0}), to: {a} = {a0}*({p}) + {b0}*({q})")
else:
    print(f"NWD({a0},{b0}), to: {a} = {a0}*{p} + {b0}*{q}")
