#! python3
import itertools
import random
import json
import os


def random_quiz_country():
    correct_answer = list()
    correct_country = list()
    final_city = list()
    with open(os.path.join(os.getcwd(), "country-capital-city.json"), "r") as f_json:
        contents = json.load(f_json)
        # print(contents)
        letter = "ABCD"
        for i in range(0, len(contents)):
            all_city = list()
            correct_city = contents[i]["city"]
            # print(correct_city)
            country = contents[i]["country"]
            # print(correct_country)
            for j in range(3):
                rand_int = random.randint(0, len(contents) - 1)
                city = contents[rand_int]["city"]
                # print(city)
                all_city.append(city)
                # print(all_city)
            all_city.append(correct_city)
            # print(all_city)
            random.shuffle(all_city)
            random_dict = {}
            for k in range(4):
                random_dict[all_city[k]] = letter[k]
            final_city += [random_dict]
            print(all_city)
            correct_answer += random_dict[correct_city]
            # print(correct_answer)
            correct_country += [country]
        total_list = [correct_country, correct_answer, final_city]
    return total_list


def play_total():
    total = 0
    my_set = random_quiz_country()
    print(my_set)
    for i, j, k in zip(my_set[0], my_set[1], my_set[2]):
        print(f"Dla kraju: {i}, stolicą jest: \n {k}.")
        capital = input(
            "Podaj A, B, C lub D. Każda inna odpowiedź będzie błędna. \n Z to wyjście z programu."
        )
        if capital == j:
            total += 1
        elif capital == "Z":
            break
        else:
            continue
    print(total)
    return str(total)
