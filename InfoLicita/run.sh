#!/bin/bash
FILES=./*xls*
rm -Rf salida.txt
for f in $FILES
do
  echo "Processing $f file..."
  python excel.py > out.txt
  python ajusta.py >> salida.txt
done

