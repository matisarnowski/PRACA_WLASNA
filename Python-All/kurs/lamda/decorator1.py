def my_decorator(func):
    def wrapper(text):
        to_return = func(text)
        print(
            "Wykonał Mateusz Sarnowski. Poszukujący pracy jako stażysta w programowaniu, w języku Python."
        )
        return to_return

    return wrapper


@my_decorator
def func(text: str) -> dict:
    dict_with_signs = {}
    special_signs = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "-",
        "+",
        "=",
        "{",
        "}",
        ":",
        ";",
        '"',
        "~",
        "`",
        "‚",
        "”",
        " ",
        "\n",
        "\t",
        "€",
        "<",
        ",",
        ">",
        ".",
        "?",
        "/",
        "„",
        "™",
        "‡",
        "¦",
        "…",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "[",
        "]",
        "¿",
    ]
    for i in text:
        if i not in special_signs:
            if i in dict_with_signs.keys():
                dict_with_signs[i] += 1
            else:
                dict_with_signs[i] = 1

    return dict_with_signs


if __name__ == "__main__":
    text = []
    with open("PS.txt", "r", encoding="utf-8") as file:
        for i in file.readlines():
            text += str(i)

    result = func(text)
    result = dict(sorted(result.items()))
    print(result)
    maximum = max(result.values())
    print(sorted(result.items(), key=lambda x: x[1]))
    print(maximum)
