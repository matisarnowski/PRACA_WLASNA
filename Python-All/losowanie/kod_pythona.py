import random

with open("loteria.txt", "w+") as loterry:
    with open("losowanie_1.txt", "w") as first:
        with open("losowanie_2.txt", "w") as second:
            tab_tmp = []
            for i in range(0, 1000):
                tab = []
                # loterry.write("Losowanie nr " + str(i + 1) + " -> ")
                for j in range(0, 5):
                    tab.append(random.randint(1, 25))
                tab_tmp.append(tab)
                for k in tab:
                    loterry.write(str(k) + " ")
                loterry.write("\n")
            tab_first, tab_second = [], []
            for l in range(0, 5):
                tab_first.append(random.randint(1, 25))
                tab_second.append(random.randint(1, 25))
            first.write("Pierwsze dodatkowe losowanie pięciu liczb. \n")
            second.write("Drugie dodatkowe losowanie pięciu liczb. \n")
            for m in tab_first:
                first.write(str(m) + " ")
            for n in tab_second:
                second.write(str(n) + " ")
            first.write("\n")
            second.write("\n")

            for count in range(0, 1000):
                total_3 = 0
                total_4 = 0
                total_5 = 0
                for o in tab_tmp[count]:
                    if (o == 3) and (3 in tab_first):
                        total_3 += 3
                    if (o == 4) and (4 in tab_first):
                        total_4 += 6
                    if (o == 5) and (5 in tab_first):
                        total_5 += 12
                if total_3 != 0 and total_4 != 0 and total_5 != 0:
                    if total_3 == min(total_3, total_4, total_5):
                        first.write('"3" - ' + str(total_3) + "\n")
                    elif total_4 == min(total_3, total_4, total_5):
                        first.write('"4" - ' + str(total_4) + "\n")
                    else:
                        first.write('"5" - ' + str(total_5) + "\n")
                elif total_3 != 0 and total_4 != 0 and total_5 == 0:
                    if total_3 == min(total_3, total_4):
                        first.write('"3" - ' + str(total_3) + "\n")
                    else:
                        first.write('"4" - ' + str(total_4) + "\n")
                elif total_3 != 0 and total_4 == 0 and total_5 != 0:
                    if total_3 == min(total_3, total_5):
                        first.write('"3" - ' + str(total_3) + "\n")
                    else:
                        first.write('"4" - ' + str(total_5) + "\n")
                elif total_3 == 0 and total_4 != 0 and total_5 != 0:
                    if total_4 == min(total_4, total_5):
                        first.write('"4" - ' + str(total_4) + "\n")
                    else:
                        first.write('"5" - ' + str(total_5) + "\n")
                elif total_3 != 0 and total_4 == 0 and total_5 == 0:
                    first.write('"3" - ' + str(total_3) + "\n")
                elif total_3 == 0 and total_4 != 0 and total_5 == 0:
                    first.write('"4" - ' + str(total_4) + "\n")
                elif total_3 == 0 and total_4 == 0 and total_5 != 0:
                    first.write('"5" - ' + str(total_5) + "\n")
                elif total_5 == 0 and total_4 == 0 and total_3 == 0:
                    first.write('"-" - 0 \n')
                total_3 = 0
                total_4 = 0
                total_5 = 0
                for o in tab_tmp[count]:
                    if (o == 3) and (3 in tab_second):
                        total_3 += 3
                    if (o == 4) and (4 in tab_second):
                        total_4 += 6
                    if (o == 5) and (5 in tab_second):
                        total_5 += 12
                if total_3 != 0 and total_4 != 0 and total_5 != 0:
                    if total_3 == min(total_3, total_4, total_5):
                        second.write('"3" - ' + str(total_3) + "\n")
                    elif total_4 == min(total_3, total_4, total_5):
                        second.write('"4" - ' + str(total_4) + "\n")
                    else:
                        second.write('"5" - ' + str(total_5) + "\n")
                elif total_3 != 0 and total_4 != 0 and total_5 == 0:
                    if total_3 == min(total_3, total_4):
                        second.write('"3" - ' + str(total_3) + "\n")
                    else:
                        second.write('"4" - ' + str(total_4) + "\n")
                elif total_3 != 0 and total_4 == 0 and total_5 != 0:
                    if total_3 == min(total_3, total_5):
                        second.write('"3" - ' + str(total_3) + "\n")
                    else:
                        second.write('"4" - ' + str(total_5) + "\n")
                elif total_3 == 0 and total_4 != 0 and total_5 != 0:
                    if total_4 == min(total_4, total_5):
                        second.write('"4" - ' + str(total_4) + "\n")
                    else:
                        second.write('"5" - ' + str(total_5) + "\n")
                elif total_3 != 0 and total_4 == 0 and total_5 == 0:
                    second.write('"3" - ' + str(total_3) + "\n")
                elif total_3 == 0 and total_4 != 0 and total_5 == 0:
                    second.write('"4" - ' + str(total_4) + "\n")
                elif total_3 == 0 and total_4 == 0 and total_5 != 0:
                    second.write('"5" - ' + str(total_5) + "\n")
                elif total_5 == 0 and total_4 == 0 and total_3 == 0:
                    second.write('"-" - 0 \n')
