<?php
try {
    include '../sql/connection.php';
    include '../sql/dbfunction.php';
    
    $answer = list_answer($pdo, $_POST['id']);
    
    $title = 'Question list';

    ob_start();
    include 'list_answer.html.php';
    $output = ob_get_clean();
} catch (PDOException $e) {
    $title = 'An error has occured';
    $output = 'Database error: ' . $e->getMessage();
}
include '../userlayout/layout.html.php';
