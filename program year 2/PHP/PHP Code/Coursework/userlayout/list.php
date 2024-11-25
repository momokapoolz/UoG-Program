<?php
try {
    include '../sql/connection.php';
    include '../sql/dbfunction.php';
    
    $questions = list_question($pdo);
    
    $title = 'Question list';

    ob_start();
    include 'list.html.php';
    $output = ob_get_clean();
} catch (PDOException $e) {
    $title = 'An error has occured';
    $output = 'Database error: ' . $e->getMessage();
}
include 'layout.html.php';
