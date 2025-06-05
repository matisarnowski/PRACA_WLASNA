#! /bin/python3

import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.create_sheet("Sheet")
italic24Font = Font(size=24, italic=True)
styleObj = NamedStyle(name="styleObj", font=italic24Font)
wb.add_named_style(styleObj)
for cell in sheet[1]:
    cell.style = "styleObj"
sheet["A1"] = "Witaj świecie!"
wb.save("styledCorrected.xlsx")
