import os
import tkinter as tk
from tkinter import messagebox


def run_app():
    main_window = tk.Tk()

    def login():
        file_name = text_var_user_name.get()
        second_text = text_var_password.get()

        if os.path.isfile(os.path.join(os.getcwd(), file_name + ".txt")):
            messagebox.showerror(
                title="Błąd dodawiania użytkownka.",
                message="Ten użytkownik już istnieje, podaj inną nazwę.",
            )
        else:
            with open(file_name + ".txt", "w") as file:
                file.write(
                    "Hasło: \n"
                    + second_text
                    + "\n"
                    + "Nazwa użytkownika: \n"
                    + file_name
                )
                messagebox.showinfo(
                    title="Dodano użytkownika.",
                    message="Twój nowy użytkownik, to, " + file_name + ".",
                )

    main_window.title("Moja aplikacja do logowania.")
    main_window.geometry("590x500")
    main_window.configure(bg="#0a0a0a")

    frame = tk.Frame(bg="#0a0a0a")

    label_login = tk.Label(frame, text="Tworzenie użytkownika!!!")
    label_login.grid(sticky="news", column=0, row=0, columnspan=2, pady=40, padx=40)
    label_login.config(fg="#33d113", bg="#f20a4f", font=("Roboto", 22))

    label_username = tk.Label(frame, text="Nazwa użytkownika:")
    label_username.grid(column=0, row=1)
    label_username.config(fg="#59d113", bg="#0a0a0a")
    label_username.config(font=("Roboto", 22))

    text_var_user_name = tk.StringVar(frame)

    entry_username = tk.Entry(frame, textvariable=text_var_user_name)
    entry_username.grid(sticky="e", column=1, row=1, pady=20)
    entry_username.config(font=("Roboto", 22))

    label_password = tk.Label(frame, text="Hasło:")  # ,justify=tk.LEFT, anchor="w")
    label_password.grid(sticky="w", column=0, row=2)
    label_password.config(fg="#33d113", bg="#0a0a0a")
    label_password.config(font=("Roboto", 22))

    text_var_password = tk.StringVar(frame)

    entry_password = tk.Entry(frame, show="*", textvariable=text_var_password)
    entry_password.grid(sticky="e", column=1, row=2, pady=20)
    entry_password.config(font=("Roboto", 22))

    button_login = tk.Button(frame, text="Utwórz nowego użytkownika.", command=login)
    button_login.grid(sticky="news", row=3, column=0, pady=40, columnspan=2)
    button_login.config(font=("Roboto", 22))

    frame.pack()

    main_window.mainloop()


run_app()
