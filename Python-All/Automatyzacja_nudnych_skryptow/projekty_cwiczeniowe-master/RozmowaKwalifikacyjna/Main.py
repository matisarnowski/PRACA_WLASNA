#!/usr/bin/python3
from Language import Language
from Requirement import Requirement


def main():
    languages = Language()
    requirements = Requirement(languages.language_dict)
    while True:
        language_name = languages.set_language_name()
        languages.write_dict_language()
        while True:
            requirements.set_requirement_name(language_name)
            requirements.write_requirements_name()
            print("Czy chcesz wyjść? T/N")
            c = input()
            if c == "T" or c == "t":
                break
            elif c == "N" or c == "n":
                continue
            else:
                print("Coś poszło nie tak.")
        print("Czy chcesz wyjść? T/N")
        c = input()
        if c == "T" or c == "t":
            break
        elif c == "N" or c == "n":
            continue
        else:
            print("Coś poszło nie tak.")


if __name__ == "__main__":
    main()
