import tkinter as tk


class Window(tk.Tk):
    def __init__(self, parent, parametr):
        self.parametr = parametr
        self.parent = parent
        self.parent.title("Okno dla szukanego tekstu! ")
        self.parent.configure(bg="green")

        self.label_text = tk.Label(
            self.parent, text="Tu podaj tekst, który ma być wyszukany: ", bg="yellow"
        )
        self.label_text.grid(row=0, column=0)

        self.varStr = tk.StringVar()
        self.entry_str = tk.Entry(self.parent, textvariable=self.varStr, fg="red")
        self.entry_str.grid(row=0, column=1)

        def clicked():
            self.parametr = True

        self.button_send_message = tk.Button(
            self.parent,
            text="Aby, wyświetlić trzy pierwsze wyniki naciśnij!",
            command=clicked,
            bg="yellow",
        )
        self.button_send_message.grid(row=1, column=0)

        self.label_text_1 = tk.Label(
            self.parent,
            text="Nie zapomnij zamknąć okna, aby wyświetlić wyniki. ",
            bg="yellow",
        )
        self.label_text_1.grid(row=1, column=1)
