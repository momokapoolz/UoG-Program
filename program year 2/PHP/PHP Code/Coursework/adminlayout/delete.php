<?php
try{
    include '../sql/connection.php';
    include '../sql/dbfunction.php';

    /*$sql = 'DELETE FROM questions WHERE id = :id';
    $stmt = $pdo->prepare($sql);
    $stmt->bindValue(':id', $_POST['id']);
    $stmt->execute();*/
    delete_question($pdo, $_POST['id']);
    header('location: list.php');
}catch(PDOException $e){
$title = 'An error has occured';
$output = 'Unable to connect to delete joke: ' .$e->getMessage();
}
include 'layout.html.php';