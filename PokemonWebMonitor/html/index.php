<html>

<form id="buscador" name="buscador" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">  
	Q: <input id="buscarIP" name="buscarIP" type="search" placeholder="Buscar aquí..." autofocus style="width: 100%;"> 
	<input type="submit" name="buscador" class="boton peque aceptar" value="buscar"> 
</form>

<?php


$ip = trim($_POST['buscarIP']);

$link = mysql_connect('localhost', 'root', 'root') or die('No se pudo conectar: ' . mysql_error());

mysql_select_db('monitor') or die('No se pudo seleccionar la base de datos');

$query = $ip;
echo ($query."<p /><br />");
$result = mysql_query($query) or die('Consulta fallida: ' . mysql_error());

echo "<table border='1'>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

mysql_free_result($result);

mysql_close($link);
?>

</html>
