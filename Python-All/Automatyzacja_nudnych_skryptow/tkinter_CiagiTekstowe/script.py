import tkinter as tk


def podaj_liczbe(writting):
    if writting == False:
        return True


def okno_destroy(pomoc, pole_tekstowe):
    if podaj_liczbe(writting.get().isalpha()) == False:
        del pole_tekstowe
        pole_tekstowe = "Musisz podać liczbę dodatnią"
        tekst.configure(text=pole_tekstowe)
    else:
        pomoc.destroy()

        def podaj_ciag(haslo_napis):
            if haslo_napis == "aaaa":
                return True
            else:
                return False

        def ostateczne_destroy(ostateczne, pole_tekstowe_1):
            if podaj_ciag(haslo_napis.get()) == False:
                del pole_tekstowe_1
                pole_tekstowe_1 = "Musisz podać prawidłowe hasło."
                tekst_1.configure(text=pole_tekstowe_1)
            else:
                ostateczne.destroy()

        def ustal_haslo():
            ostateczne_destroy(ostateczne, pole_tekstowe_1)

        ostateczne = tk.Tk()
        ostateczne.title("Podaj już tylko hasło!")
        haslo_napis = tk.StringVar()
        pole_tekstowe_1 = "Podaj swoje hasło: "
        tekst_1 = tk.Label(ostateczne, text=pole_tekstowe_1)
        tekst_1.grid(row=0, column=0)
        haslo = tk.Entry(ostateczne, textvariable=haslo_napis)
        haslo.grid(row=1, column=0)
        button_1 = tk.Button(
            ostateczne,
            text="Zamknij, jeśli podałeś już hasło.",
            width=25,
            command=ustal_haslo,
        )
        button_1.grid(row=2, column=0)
        ostateczne.mainloop()


def ustal_wiek():
    okno_destroy(pomoc, pole_tekstowe)


pomoc = tk.Tk()

pomoc.title("Podaj wiek i hasło!")
writting = tk.StringVar()
pole_tekstowe = "Podaj swój wiek: "
tekst = tk.Label(pomoc, text=pole_tekstowe)
tekst.grid(row=0, column=0)
wiek = tk.Entry(pomoc, textvariable=writting)
wiek.grid(row=1, column=0)
button = tk.Button(
    pomoc, text="Zamknij, jeśli podałeś wiek.", width=25, command=ustal_wiek
)
button.grid(row=2, column=0)

pomoc.mainloop()
