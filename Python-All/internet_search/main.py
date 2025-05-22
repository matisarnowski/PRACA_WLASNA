import requests
import webbrowser
import bs4
from my_tknter import *


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = Window(root, False)
    root.mainloop()

    if my_gui.parametr:
        print("Wyszukiwanie...")
        res = requests.get(
            "http://google.pl/search?q=" + "".join(str(my_gui.varStr.get()))
        )
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="lxml")

        linkElems = soup.select("div#main > div > div > div > a")
        numOpen = min(3, len(linkElems))
        for i in range(numOpen):
            webbrowser.open("http://google.pl" + linkElems[i].get("href"))
