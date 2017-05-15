#!/usr/bin/env python
import openpyxl

_author_ = "rifatul.islam"

wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet1')
val = sheet['A1']
print(str(val.row))
print(str(val.column))
print(str(val.coordinate))
print(str(val.value))
