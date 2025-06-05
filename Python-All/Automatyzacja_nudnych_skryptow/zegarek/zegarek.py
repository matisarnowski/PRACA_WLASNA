#!/usr/bin/python3

import time
import tkinter as tk
import locale


def update_time():
    now = time.strftime("%H: %M")
    lbl_now.configure(text=now)
    today = time.strftime("%A %B %d")
    lbl_today.configure(text=today)
    window.update()
    window.after(5000, update_time)


window = tk.Tk()
locale.setlocale(locale.LC_TIME, "pl_PL.UTF-8")
lbl_now = tk.Label(window, text="", font=("Helvetica", 128))
lbl_now.pack()
lbl_today = tk.Label(window, text="", font=("Helvetica", 64))
lbl_today.pack()
btn = tk.Button(
    window, text="CLOSE!", font=("Helvetica", 32), bg="grey", command=window.destroy
)
btn.pack()

window.title("Mój zegarek.")
window.attributes("-fullscreen")
window.after(1000, update_time)
window.mainloop()
