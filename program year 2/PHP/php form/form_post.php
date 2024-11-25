<?php
$username = $_POST['username'];
$password = $_POST['password'];
$gender = $_POST['Gender'];
if ($username == 'admin' && $password == '123456789')
    echo "login succeed" . $gender . "<br>"; 
else
    echo "login failed";



?>