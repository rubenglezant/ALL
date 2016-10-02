<?php
//-----------------------------------------------------
$numDias = 15;
$fechaComienzo ='2015-12-12';

$tipoInforme['Numero de Atascos Billetero']='%Jam%';
$tipoInforme['Numero de Tickets Impresos']='%Impresion Ticket%';
$tipoInforme['Numero de Atascos Impresora']='%atasco%';
$tipoInforme['Puerta Principal Abierta']='%puerta principal abierta%';
$tipoInforme['Impresora Sin Papel']='%sinPapel%';
$tipoInforme['EMV no Disponible']='%EMV no disponibl%';
$tipoInforme['Pagos con EMV']='%Pago EMV ok%';
$tipoInforme['Aperturas del Aceptador de Billetes']='%billetes aceptador abierto%';
$tipoInforme['Billetes Deteriorados']='%Estado de Billete deteriorado%';
$tipoInforme['Atasco en Validador']='%Jam en validador%';
$tipoInforme['Aperturas de la Puerta del Hopper']='%puerta hoppers abierta%';
$tipoInforme['Aperturas de la Caja de Monedas']='%caja de monedas abierta%';
$tipoInforme['Eventos de Caja Llena']='%Caja llena%';
$tipoInforme['Eventos de Efectivo No Disponible']='%Efectivo no disponible%';
$tipoInforme['Recaudaciones Realizadas']='%Recaudaci%';


//-----------------------------------------------------
$host="localhost";
$port=3306;
$socket="";
$user="root";
$password="root";
$dbname="finalMonitor";

$con = new mysqli($host, $user, $password, $dbname, $port, $socket)
	or die ('Could not connect to the database server' . mysqli_connect_error());

printf("<html>\n");
printf("<body>\n");

// Para cada Tabla
foreach($tipoInforme as $tipoInformeDescripcion=>$tipoInformeFiltro){
	$tabla = array();
	$fechaArray = array();

	$query = "select distinct(IP) from eventos";

	if ($stmt = $con->prepare($query)) {
	    $stmt->execute();
	    $stmt->bind_result($IP);
	    while ($stmt->fetch()) {
		$tabla[$IP]=array();
	    }
	    $stmt->close();
	}

	$fecha = date_create($fechaComienzo);

	echo ("<h1>".$tipoInformeDescripcion."</h1>");

	for ($i = 1; $i <= $numDias; $i++) {
		$fechaOld = date_format($fecha, 'Y-m-d');
		date_add($fecha, date_interval_create_from_date_string('1 days'));
		$fechaNew = date_format($fecha, 'Y-m-d');
		$fechaArray[$i] = $fechaNew;

		$query = "SELECT IP, count(*) as valor   FROM eventos  WHERE TIMESTAMP_ACTIVA>='".$fechaOld."'    AND TIMESTAMP_ACTIVA< '".$fechaNew."'    AND DESCRIPCION like '".$tipoInformeFiltro."' GROUP BY IP ORDER BY IP DESC";

		if ($stmt = $con->prepare($query)) {
		    $stmt->execute();
		    $stmt->bind_result($IP, $valor);
		    while ($stmt->fetch()) {
			//printf("%s, %s\n", $IP, $valor);
			$tabla[$IP][$i]=$valor;
		    }
		    $stmt->close();
		}
		//$con->close();
	}


	printf("<table border='1'>\n");
	printf("<tr><td>Fecha</td>");
	for ($i = 1; $i <= $numDias; $i++) {
		$valor=$fechaArray[$i];
		printf("<td>%s</td>", $valor);
	}
	printf("</tr>\n");

	foreach($tabla as $person=>$id){
		printf("<tr><td>%s</td>", $person);
		for ($i = 1; $i <= $numDias; $i++) {
			if(array_key_exists($i, $id)){
				$valor=$id[$i];
				printf("<td><center>%s</center></td>", $valor);
			} else{
				printf("<td></td>");
			}
		}
		printf("</tr>\n");
	}
	printf("</table>\n");
}
	
printf("</body>\n");
printf("</html>\n");

?>

