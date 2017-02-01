<?php 
// Set the JSON header
header("Content-type: text/json");

$username="root";
$password="raspberry";
$database="sensor_database";

mysql_connect(localhost,$username,$password);
@mysql_select_db($database) or die( "Unable to select database");
$query="SELECT * FROM plant_log";
$result=mysql_query($query);
$tempRow=mysql_numrows($result)-3;
$lightRow=mysql_numrows($result)-2;
$moistRow=mysql_numrows($result)-1;
mysql_close();
$tempReading = mysql_result($result,$tempRow,"Temp");
$lightReading = mysql_result($result,$lightRow,"Light");
$moistReading = mysql_result($result,$moistRow,"Moist");

// The x value is the current JavaScript time, which is the Unix time multiplied by 1000.
$x = time() * 1000;
// Create a PHP array and echo it as JSON
$ret = array(array($x, (int)$tempReading), array($x, (int)$lightReading), array($x, (int)$moistReading));
echo json_encode($ret);
?>
