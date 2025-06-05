def sum_all(*args) -> None:
    total = 0
    for i in args:
        total += i
    print(total)


def show_text(a: str, b: str, **kwargs) -> None:
    if kwargs.get("show_upper", False):
        print(a.upper(), b.upper())
    else:
        print(a, b)

    if kwargs.get("show_lower", False):
        print(a.lower(), b.lower())


if __name__ == "__main__":
    sum_all(10)
    sum_all(11, 9)
    sum_all()
    sum_all(1, 2, 3, 4, 5, 6)
    sum_all(1, 2, 3, 4)
    print()
    show_text("kot", "pies", show_lower=True)
    show_text("kot", "pies", show_upper=True)
