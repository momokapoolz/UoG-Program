<?php
if(isset($_POST['book_title'])){
    try{
        include 'includes/connection.php';
        $sql = 'INSERT INTO books SET
        book_title = :book_title';
        $stmt = $pdo->prepare($sql);
        $stmt->bindValue(':book_title', $_POST['book_title']);
        $stmt->execute();
        header('location: listbook.php');
    }catch (PDOException $e){
        $title = 'An error has occurred';
        $output = 'Database error: ' . $e->getMessage();
    }
}else{
    include 'includes/connection.php';
    $sql = "SELECT * FROM genres";
    $genres = $pdo->query($sql);
    $title = 'Add a new book';
    ob_start();
    include 'templates/addbook.html.php';
    $output = ob_get_clean();
}
include 'templates/layout.html.php';
