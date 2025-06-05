#! /usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("produceSales.xlsx")
sheet = wb["Sheet"]
sheet.freeze_panes = "A2"
wb.save("produceSales.xlsx")
