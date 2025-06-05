import os
import tkinter as tk
from tkinter import filedialog

import PyPDF2


def openFile():
    file_name = filedialog.askopenfilename(
        title="Otwórz plik PDF.",
        initialdir=os.getcwd(),
        filetypes=[("Pliki PDF", "*.pdf")],
    )
    label_file_name.configure(text=file_name)
    out_of_file_text.delete("1.0", tk.END)
    reader = PyPDF2.PdfReader(file_name)

    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        out_of_file_text.insert(tk.END, current_text)


main_window = tk.Tk()
main_window.title("Ekstrakcja tekstu z pliku PDF.")
main_window.geometry("500x600")
main_window.config(bg="#121211")

label_file_name = tk.Label(
    main_window, text="Nie wybrano żadnego plikiu do ekstrakcji danych."
)
label_file_name.config(bg="#121211", fg="#33f707", font=("Roboto", 14))
label_file_name.pack(side=tk.TOP)

out_of_file_text = tk.Text(main_window)
out_of_file_text.config(bg="#121211", fg="#33f707", font=("Roboto", 14))
out_of_file_text.pack()

button_open_file = tk.Button(main_window, text="Otwórz plik PDF", command=openFile)
button_open_file.config(bg="#121211", fg="#33f707", font=("Roboto", 14))
button_open_file.pack(side=tk.BOTTOM)

main_window.mainloop()
