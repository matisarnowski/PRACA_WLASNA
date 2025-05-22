import tkinter as tk
from myFiles import *


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.variable = tk.StringVar()

        # self.size_variable = tk.StringVar()

        self.label = tk.Label(textvariable=self.variable)
        self.label.pack()

        self.entry = tk.Entry(textvariable=self.variable)
        self.entry.pack()
