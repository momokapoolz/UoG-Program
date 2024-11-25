<?php

/*
dbname: database name, host = localhost, database username:root, password is empty
*/

try {
    $connection = new PDO('mysql:host=localhost; dbname=greenwich; charset=utf8mb4', 'root', '');
    $result = 'Success connected';  
    $sql = 'SELECT * FROM student';
    $show = $connection->query($sql);
}
catch (PDOException $ex){
    $result = 'Fail' . $ex->getMessage();
}  

include 'output.html.php'

?>