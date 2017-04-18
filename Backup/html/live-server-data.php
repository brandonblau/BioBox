<?php 
// Set the JSON header
header("Content-type: text/json");

$username="root";
$password="raspberry";
$database="sensor_database";


mysql_connect("localhost",$username,$password);
@mysql_select_db($database) or die( "Unable to select database");
$query="SELECT * FROM plant_log";
$result=mysql_query($query);
$tempRow=1;
$lightRow=2;
$moistRow=3;
$humidRow=4;
//$row = mysql_fetch_array($result, MYSQL_NUM);
//echo $row[1];
//echo $row[2];
//echo $row[3];
//echo $row[4];

//for($i = 0; $i<sizeof($row); $i++) {
//   echo $row[i];
//}

$tempReading = mysql_result($result,$tempRow,"Temp");
$lightReading = mysql_result($result,$lightRow,"Light");
$moistReading = mysql_result($result,$moistRow,"Moist");
$humidReading = mysql_result($result,$humidRow,"Humidity");

// The x value is the current JavaScript time, which is the Unix time multiplied by 1000.
$x = time() * 1000;
// Create a PHP array and echo it as JSON
$ret = array(array($x, (int)$tempReading), array($x, (int)$lightReading), array($x, (int)$moistReading), array($x, (int)$humidReading));
echo json_encode($ret);
?>
