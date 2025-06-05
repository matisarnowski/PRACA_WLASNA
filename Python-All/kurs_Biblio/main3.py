def my_sqrt(x: int) -> float:
    return round(x**0.5, 4)


def my_increment(x: int) -> int:
    return x + 1


def run_function(func, value):
    return func(value)


if __name__ == "__main__":
    print(run_function(my_sqrt, 2))
    print(run_function(my_increment, 100))
