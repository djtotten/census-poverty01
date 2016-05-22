
'''
indent(df) -- adds columns according to the indentation level of column IndentLevel.

*** SET UP THE EXCEL SPREADSHEET WITH A COLUMN NAMED IndentLevel:

http://professor-excel.com/how-to-return-the-indentation-of-a-cell-in-excel/

In the excel spreadsheet, create a column named IndentLevel then in each cell in that
colum run  macro PROFEXIndentLevel. E.g. Say original excel col A is indented, and the header
row is row 1:
   - Insert Col A. The orig col A now is Col B.
   - At A1, place name 'IndentLevel'
   - At A2, place =PROFEXIndentLevel(B2)  # No indent is 0.
   - Copy A2 and paste thru the last cell in A2 that has a value in col B.

*** In python script:

xlsfile = pd.ExcelFile(name of the xlsx or xlsm file)
df = xlsfile.parse(sheet_name {other args})
djtlib:indent(df) # Add new cols based on the indentations in the IndentLevel column.

'''
def indent ( df ):
    ic = df['IndentLevel']
    for il in df['IndentLevel']:
        print il
    return ic