<?php
try {
    include 'connectsql.php';
    $sql = 'SELECT * FROM employee';
    $employee = $pdo->query($sql);

    ob_start();
    include 'view.html.php';
    $output = ob_get_clean();

}catch (PDOException $e){
    $title = 'An error has occured';
    $output= 'Database error: ' . $e->getMessage();
}

include 'layout.html.php';
?>