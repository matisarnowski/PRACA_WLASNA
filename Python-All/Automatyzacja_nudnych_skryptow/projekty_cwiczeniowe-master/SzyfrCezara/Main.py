#!/usr/bin/python3
from Key import Key
from Text import Text
from Encryption import Encryption


def main():
    encryption = Encryption()
    encryption_valid = encryption.get_encryption()
    print(encryption_valid)


if __name__ == "__main__":
    main()
