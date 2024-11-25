<?php
$pdo = new PDO('mysql:host=localhost; dbname=week6_db; charset=utf8mb4','root', '');
try {
    $sql = 'SELECT * FROM category';
    $category = $pdo->query($sql);

}catch (PDOException $e){
    $title = 'An error has occured';
    $output= 'Database error: ' . $e->getMessage();
}

include 'view_category.html.php';
?>