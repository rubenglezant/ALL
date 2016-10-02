#Used to make requests
from datetime import datetime, date, time, timedelta
from time import sleep
import urllib.request
import calendar

def getDataURL(idVehiculo, hoy, ayer, f):
    url = 'https://csv.business.tomtom.com/extern?account=FerroSer&username=iecisa&password=piloto1&action=showTracks&apikey=4b2f7c38-2f3f-4b0d-91b3-a462a6385d49&outputformat=csv&lang=en&range_pattern=ud&rangefrom_string='+ayer+'&rangeto_string='+hoy+'&objectuid='+idVehiculo

    # Obtenemos los valores de la URL
    x = urllib.request.urlopen(url)
    data = str(x.read())

    # Ajustamos la al formato CSV PURO
    data = data.replace("\'","")
    data = data.replace("\"","")
    data = data[1:]
    data = data.replace("pos_time;receivetime;latitude;longitude;speed;course;roadtype;roadspeedlimit;fuelusage;iqr_avg_speed;iqr_freeflow_speed;odometer;country;state;incity\\r\\n","")

    # Annadimos el idVehiculo
    data = data.replace("\\r\\n",idVehiculo+";\n")

    if (data.find("document contains no data")<0):
        f.write(data)
    else:
        print ("No hay datos")

    return

# ------------------ Principal -----------------------
# Apertura
f = open('data.txt','w')

vehicles = ["1-83646-6667686335","1-83646-6667686380","1-83646-466769142C","1-83646-72131DB646","1-83646-72131DBA42","1-83646-05040A1200","1-83646-19686C3111","1-83646-2998996E60","1-83646-9594911FAD","1-83646-29989963B0"]

for idVehiculo in vehicles:
    # Preparamos las fechas
    formato = "%d/%m/%Y %H:%M:%S"  # Asigna un formato de ejemplo2
    hoy = datetime.today()
    hoy = hoy.replace(hour=23, minute=59, second=59)
    # hoy = hoy.replace(day=14, month=7)
    a = timedelta(days=2)

    # Vamos recorriendo las fechas dia a dia hacia atras
    for i in range(1,50):
        ayer = hoy-a
        cadenaHoy = (hoy.strftime(formato).replace(" ","%20"))
        cadenaAyer = (ayer.strftime(formato).replace(" ","%20"))
        hoy = ayer

        print (cadenaHoy + " " + idVehiculo+ " " + str(i))

        # Recogemos los datos y escribimos en el fichero
        # idVehiculo = '1-83646-466769142C'
        getDataURL(idVehiculo,cadenaHoy,cadenaAyer,f)

        sleep(5)

# Cierre
f.close()