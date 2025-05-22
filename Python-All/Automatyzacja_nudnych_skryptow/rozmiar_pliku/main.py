from myFiles import *
from myWindow import *


def main():
    my_calculate = MyCalculate()
    suma = 0
    root = tk.Tk()
    root.mainloop()
    myapp = App(root)
    my_calculate.path = os.path.join(myapp.variable.get())
    suma = my_calculate.size_recursive_directory()
    myapp.size_variable = suma
    myapp.update()

    myapp.mainloop()


if __name__ == "__main__":
    main()
