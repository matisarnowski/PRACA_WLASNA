#! /usr/bin/python3

import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
sheet["A1"] = "Wysoki wiersz"
sheet["B2"] = "Szeroka kolumna"
sheet.row_dimensions[1].height = 70
sheet.column_dimensions["B"].width = 20

wb.save("dimensionsCorrected.xlsx")
