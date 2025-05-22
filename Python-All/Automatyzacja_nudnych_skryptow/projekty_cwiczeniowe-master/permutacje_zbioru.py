n = int(input())

for i in range(1, n + 1):
    print(str(i))
    for j in range(i + 1, n + 1):
        print(str(j))
        for k in range(i + j, n + 1):
            print(str(k))
            print(str(i) + str(j))
            print(str(j) + str(k))
            print(str(i) + str(k))
            print(str(i) + str(j) + str(k))
