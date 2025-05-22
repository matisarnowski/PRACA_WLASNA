import os


class MyCalculate:
    def __init__(self, suma: int = 0, path=os.getcwd()) -> None:
        self.suma = suma
        self.path = path

    def size_recursive_directory(self):
        self.suma = 0
        for path, files in os.walk(self.path):
            for f in files:
                file = os.path.join(path, f)
                if not os.path.islink(file):
                    self.suma += os.path.getsize(file)
        return self.suma
