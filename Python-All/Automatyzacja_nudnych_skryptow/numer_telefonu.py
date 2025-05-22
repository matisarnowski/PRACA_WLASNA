#! /usr/bin/python3

import re

phoneNumber = re.compile(r"\d\d \d\d\d-\d\d\d-\d\d\d")
text = "48 111-942-703"
find = phoneNumber.search(text)
print("Your phone number is: " + find.group())
