import openpyxl

# ファイルを開く
wb = openpyxl.load_workbook( "0729.xlsx" )

# シートを開く
ws = wb[ "Sheet" ]

# D5( row=5, column=4 )に、hebi と書く
ws.cell( row=5, column=4 ).value = "hebi"

# ファイルを保存する
wb.save( "0729.xlsx" )
