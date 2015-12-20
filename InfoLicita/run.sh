#!/bin/bash
FILES=*xls*
rm -Rf salida.txt
for f in $FILES
do
  echo "Processing $f file..."
  ssconvert -O 'separator=| format=raw' "$f" out.txt
  cat out.txt >> salida.txt
done
cat salida.txt | sort | uniq > salidaSortUniq.txt

