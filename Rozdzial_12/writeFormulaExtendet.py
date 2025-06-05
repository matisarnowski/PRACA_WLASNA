#! /usr/bin/python3

import openpyxl

wbFormula = openpyxl.load_workbook("writeFormula.xlsx")
sheet = wbFormula["Sheet"]
print(sheet["A3"].value)

wbDataOnly = openpyxl.load_workbook("writeFormula.xlsx", data_only=True)
sheet_data = wbDataOnly["Sheet"]
print(sheet_data["A3"].value)
