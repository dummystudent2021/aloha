import openpyxl

wb = openpyxl.load_workbook( "0805.xlsx" )
ws_hello = wb["hello"]
print( ws_hello.cell( row=1, column=1 ).value )

