<?php
# created by Ali Garivani
$os_name = $_POST['OsName'];
$os_version = $_POST['OsVersion'];
$user_name = $_POST['UserName'];
$time_zone = $_POST['TimeZone'];
$client_ip = $_POST['Ip'];

$data = array('OsName' => $os_name,'OsVersion' => $os_version , 'TimeZone' => $time_zone, 'Ip' => $client_ip , 'UserName' => $user_name);
$json_data = json_encode($data);

$my_file = fopen('data.json', 'w');
fwrite($my_file, $json_data);
fclose($my_file);

?>