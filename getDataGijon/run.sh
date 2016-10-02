cd .

FILE="backup_$(date +%Y%m%d_%H%M%S).json"
wget http://datos.gijon.es/doc/transporte/busgijontr.json -O$FILE

HORA="$(date +%H)"
echo $HORA
if [ "$HORA" == "23" ]; then
	FILE="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
	tar -czvf $FILE *.json
	rm -Rf *.json
else
	echo "ACCESS DENIED!"
fi


