import requests
import time


class UrlLotto:
    def get_url(self):
        url = requests.get("http://www.mbnet.com.pl/dl.txt")
        return url.text

    def how_much_lines(self):
        lines = len(self.get_url())
        return lines

    def open_and_write_url(self):
        file = open("Help.txt", "w")
        file.write(self.get_url())

        with open("Help.txt") as file:
            my_list_lotto = []
            i = 0
            for line in file:
                first_index = line.rfind(" ")
                last_index = line.find("\r")
                my_str = line[first_index + 1 : last_index]
                my_list = my_str.split(",")
                my_list_lotto += [my_list]
                i += 1

        file.close()
        return my_list_lotto
