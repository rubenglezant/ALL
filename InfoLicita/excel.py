# Ejemplo de lectura de hoja Excel
import xlrd

book = xlrd.open_workbook("IECISA - 181215 - TODO.xls")
#print "The number of worksheets is", book.nsheets
#print "Worksheet name(s):", book.sheet_names()

sh = book.sheet_by_index(0)
#print sh.name, sh.nrows, sh.ncols
filas = sh.nrows
cols = sh.ncols
for x in range(1,filas):
	s = "";
	for y in range(cols):
		try:
			print (sh.cell_value(rowx=x, colx=y));
		except:
			print ("");
	print ("-----------------------");

