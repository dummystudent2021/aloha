import openpyxl

wb = openpyxl.load_workbook("ALOHA.xlsx")

print( len( wb.worksheets ) )
print( 'aloha' )

