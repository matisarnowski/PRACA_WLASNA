#! /usr/bin/python3

import random

play = "yes"

given = []
drawn = []

while play == "yes":
    for i in range(6):
        given.append(int(input("Enter the number, number:" + str(i + 1) + ": ")))
        drawn.append(random.randint(1, 50))
    hit = 0
    for j in given:
        for k in drawn:
            if j == k:
                hit += 1
    print("Your score is: " + str(hit))
    print("Drawn numbers: ")
    for l in drawn:
        print(l)
    given.clear()
    drawn.clear()

    play = input("Do you want to play again? (yes/not): ")
