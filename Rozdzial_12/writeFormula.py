#! /usr/bin/python3

import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
sheet["A1"] = 200
sheet["A2"] = 300
sheet["A3"] = "=SUM(A1:A2)"
wb.save("writeFormula.xlsx")
