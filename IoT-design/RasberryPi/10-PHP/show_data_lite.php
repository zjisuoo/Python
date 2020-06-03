<html>
<head>
<title>Database Data</title>
<meta http-equiv="refresh" content="10" >
</head>
<body>

Press button to remove the table data
<br>
<input type="button" onclick="location.href = 'del_data_lite.php';" value="Delete">
<br><br>
<b>Recorded Data</b><br>
<?php
$db = new PDO("sqlite:/var/databases/mydatabase.db");
//SQL query
$strSQL = "SELECT * FROM recordeddata WHERE itm_name LIKE 'Temp%'";
//Excute the query
$response = $db->query($strSQL);
//Loop through the response
while($column = $response->fetch())
{
   //Display the content of the response
   echo $column[0] . " ";
   echo $column[1] . " ";
   echo $column[2] . " ";
   echo $column[3] . "<br />";
}
?>
Done
</body>
</html>
