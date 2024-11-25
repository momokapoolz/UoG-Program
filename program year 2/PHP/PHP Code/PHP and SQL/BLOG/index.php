<?php

/*
dbname: database name, host = localhost, database username:root, password is empty
*/

try {
    $connection = new PDO('mysql:host=localhost; dbname=blog; charset=utf8mb4', 'root', '');
    $result = 'Success connected';  
    $sql = 'SELECT * FROM posts';
    $output = $connection->query($sql);  
}
catch (PDOException $ex){
    $result = 'Connected fail' . $ex->getMessage();
}  

include 'index.html.php';
?>