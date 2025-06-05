if __name__ == "__main__":
    func = lambda x: x + 5
    print(func(10))

    print((lambda x, y: True if y % x == 0 else False)(12, 5))
