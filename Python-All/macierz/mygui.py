from matrix_main import *
import tkinter as Tk


class Mygui:
    def __init__(
        self,
        geometry="800x800",
        title="Obliczenia na macierzach. ",
        text="",
        text2="",
        numbers=[],
        matrix=[],
    ):
        super().__init__()
        self.parent = Tk.Tk()
        self.geometry = geometry
        self.title = title
        self.text = text
        self.text2 = text2
        self.numbers = numbers
        self.matrix = matrix
        self.frame = Tk.Frame(self.parent)
        self.frame.pack()
        self.lbl = Tk.Label(
            self.frame,
            text="Podaj wartość z klawiatury, \n jakąś liczbę, inaczej się nie uda.",
        )
        self.lbl.grid(row=0, column=0)
        self.text = Tk.Text(self.frame, height=10, width=10)
        self.text.grid(row=1, column=0)
        self.lbl2 = Tk.Label(self.frame, text="Oto wartości, które wprowadziłeś:")
        self.lbl2.grid(row=0, column=1)
        self.text2 = Tk.Text(self.frame, height=10, width=10)
        self.text2.grid(row=1, column=1)
        self.btn = Tk.Button(
            self.frame, text="Wyślij!", command=self.send_data_to_matrix
        )
        self.btn.grid(row=2, column=0)

        self.lbl_with_matrix = Tk.Label(self.frame, text="Tutaj znajduje się macierz")
        self.lbl_with_matrix.grid(row=0, column=2)
        self.text_with_matrix = Tk.Text(self.frame, height=10, width=10)
        self.text_with_matrix.grid(row=1, column=2)
        self.btn_to_make_matrix = Tk.Button(
            self.frame, text="Twórz macierz!", command=self.transforme_to_matrix
        )
        self.btn_to_make_matrix.grid(row=2, column=2)

        self.lbl_change_columns_a = Tk.Label(self.frame, text="Kolumna a")
        self.lbl_change_columns_a.grid(row=0, column=3)
        self.text_change_columns_input_a = Tk.Text(self.frame, height=2, width=2)
        self.text_change_columns_input_a.grid(row=1, column=3)
        self.lbl_change_columns_b = Tk.Label(self.frame, text="Kolumna b")
        self.lbl_change_columns_b.grid(row=0, column=4)
        self.text_change_columns_input_b = Tk.Text(self.frame, height=2, width=2)
        self.text_change_columns_input_b.grid(row=1, column=4)
        self.text_change_columns_output = Tk.Text(self.frame, height=10, width=10)
        self.text_change_columns_output.grid(row=1, column=5)
        self.btn_change_columns = Tk.Button(
            self.frame, text="Zamień kolumny.", command=self.change_columns
        )
        self.btn_change_columns.grid(row=2, column=5)

        self.lbl_change_rows_a = Tk.Label(self.frame, text="Wiersz a")
        self.lbl_change_rows_a.grid(row=0, column=6)
        self.text_change_rows_input_a = Tk.Text(self.frame, height=2, width=2)
        self.text_change_rows_input_a.grid(row=1, column=6)
        self.lbl_change_rows_b = Tk.Label(self.frame, text="Wiersz b")
        self.lbl_change_rows_b.grid(row=0, column=7)
        self.text_change_rows_input_b = Tk.Text(self.frame, height=2, width=2)
        self.text_change_rows_input_b.grid(row=1, column=7)
        self.text_change_rows_output = Tk.Text(self.frame, height=10, width=10)
        self.text_change_rows_output.grid(row=1, column=8)
        self.btn_change_rows = Tk.Button(
            self.frame, text="Zamień wiersze.", command=self.change_rows
        )
        self.btn_change_rows.grid(row=2, column=8)

        self.lbl_with_matrix_transpose = Tk.Label(
            self.frame, text="Tutaj znajduje się \n macierz transponowana."
        )
        self.lbl_with_matrix_transpose.grid(row=0, column=9)
        self.text_with_matrix_transpose = Tk.Text(self.frame, height=10, width=10)
        self.text_with_matrix_transpose.grid(row=1, column=9)
        self.btn_to_make_matrix_transpose = Tk.Button(
            self.frame, text="Transponuj macierz!", command=self.transposition_matrix
        )
        self.btn_to_make_matrix_transpose.grid(row=2, column=9)

        self.lbl_with_sum_of_diagonal = Tk.Label(
            self.frame, text="Tutaj znajduje się \n suma liczb na głównej przekątnej."
        )
        self.lbl_with_sum_of_diagonal.grid(row=0, column=10)
        self.text_with_sum_of_diagonal = Tk.Text(self.frame, height=5, width=5)
        self.text_with_sum_of_diagonal.grid(row=1, column=10)
        self.btn_to_make_sum_of_diagonal = Tk.Button(
            self.frame, text="Licz sumę!", command=self.sum_of_diagonal
        )
        self.btn_to_make_sum_of_diagonal.grid(row=2, column=10)

    def send_data_to_matrix(self):
        self.text2.delete(1.0, 2.0)
        try:
            number = float(self.text.get("1.0", "end"))
            self.numbers.append(number)
            self.text2.insert("1.0", str(self.numbers))
        except Exception as e:
            self.text2.insert(
                "1.0", "Podałeś nieprawidłową wartość, spróbój jeszcze raz. \n" + str(e)
            )
        self.text.delete(1.0, 2.0)

    def transforme_to_matrix(self):
        self.text_with_matrix.delete(1.0, 2.0)
        matrix_main = Matrix_main(self.numbers)
        matrix_main.matrix = matrix_main.to_matrix()
        self.matrix = matrix_main.matrix

        self.text_with_matrix.insert("1.0", str(self.matrix))

    def change_columns(self):
        def change_places_columns_in_matrix(matrix, column_a, column_b):
            matrix[:, [column_a, column_b]] = matrix[:, [column_b, column_a]]
            return matrix

        self.text_change_columns_output.delete(0.0, 2.0)
        try:
            column_a = int(self.text_change_columns_input_a.get("1.0", "end"))
            column_b = int(self.text_change_columns_input_b.get("1.0", "end"))
            self.matrix = change_places_columns_in_matrix(
                self.matrix, column_a, column_b
            )
            self.text_change_columns_output.insert("1.0", str(self.matrix))
        except Exception as e:
            self.text_change_columns_output.insert("1.0", str(e))
        self.text_change_columns_input_a.delete(1.0, 2.0)
        self.text_change_columns_input_b.delete(1.0, 2.0)

    def change_rows(self):
        def change_places_rows_in_matrix(matrix, row_a, row_b):
            matrix[[row_a, row_b]] = matrix[[row_b, row_a]]
            return matrix

        self.text_change_rows_output.delete(0.0, 2.0)
        try:
            row_a = int(self.text_change_rows_input_a.get("1.0", "end"))
            row_b = int(self.text_change_rows_input_b.get("1.0", "end"))
            self.matrix = change_places_rows_in_matrix(self.matrix, row_a, row_b)
            self.text_change_rows_output.insert("1.0", str(self.matrix))
        except Exception as e:
            self.text_change_rows_output.insert("1.0", str(e))
        self.text_change_rows_input_a.delete(1.0, 2.0)
        self.text_change_rows_input_b.delete(1.0, 2.0)

    def transposition_matrix(self):
        self.text_with_matrix_transpose.delete(1.0, 2.0)

        def transposition(matrix):
            matrix = np.transpose(matrix)
            return matrix

        self.matrix = transposition(self.matrix)
        self.text_with_matrix_transpose.insert("1.0", str(self.matrix))

    def sum_of_diagonal(self):
        self.text_with_sum_of_diagonal.delete(1.0, 2.0)
        sum = 0

        def sum_of_diagonal(matrix):
            return np.trace(matrix)

        sum = sum_of_diagonal(self.matrix)
        self.text_with_sum_of_diagonal.insert("1.0", str(sum))
