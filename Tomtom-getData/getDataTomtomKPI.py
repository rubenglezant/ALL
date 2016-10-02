#Used to make requests
from datetime import datetime, date, time, timedelta
from time import sleep
import urllib.request
import calendar

def getDataURL(idVehiculo, indice, f):
    #url = 'https://csv.business.tomtom.com/extern?account=FerroSer&username=iecisa&password=piloto1&action=showTracks&apikey=4b2f7c38-2f3f-4b0d-91b3-a462a6385d49&outputformat=csv&lang=en&range_pattern=ud&rangefrom_string='+ayer+'&rangeto_string='+hoy+'&objectuid='+idVehiculo
    url = 'https://csv.business.tomtom.com/extern?lang=es&account=FerroSer&username=iecisa&password=piloto1&action=getObjectKPIs&apikey=4b2f7c38-2f3f-4b0d-91b3-a462a6385d49&outputformat=csv&objectuid='+idVehiculo+'&kpinames=tripstats,ecostats,optidrive,speedingevents,drivingevents,orders&level=day&range_pattern=m-'+str(indice)

    # Obtenemos los valores de la URL
    x = urllib.request.urlopen(url)
    data = str(x.read())

    # Ajustamos la al formato CSV PURO
    data = data.replace("\'","")
    data = data.replace("\"","")
    data = data[1:]

    data = data.replace("objectno;objectuid;objectname;year;month;day;externalid;drivingevents_avg_severity;drivingevents_braking_avg_severity;drivingevents_braking_count;drivingevents_count;drivingevents_forward_avg_severity;drivingevents_forward_count;drivingevents_steering_avg_severity;drivingevents_steering_count;ecostats_co2emission;ecostats_fuelusage;ecostats_idletime;ecostats_overrevvingtime;ecostats_wastedfuel;optidrive_indicator;optidrive_indicator_driving;optidrive_indicator_fuel;optidrive_indicator_idling;optidrive_indicator_speeding;orders_cancelled;orders_completed;orders_ontime;speedingevents_avg_violation;speedingevents_count;speedingevents_speedingtime;tripstats_count;tripstats_drivingtime;tripstats_mileage;tripstats_mileagebusiness;tripstats_mileageprivate;tripstats_usagetime\\r\\n","")

    # Annadimos el idVehiculo
    data = data.replace("\\r\\n",";"+idVehiculo+";\n")

    # print (data)

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

    # Vamos recorriendo los meses
    for i in range(1,4):

        print (" " + idVehiculo+ " " + str(i))

        # Recogemos los datos y escribimos en el fichero
        # idVehiculo = '1-83646-466769142C'
        getDataURL(idVehiculo,i,f)

        sleep(5)

# Cierre
f.close()