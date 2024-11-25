<?php
try {
    include 'includes/connection.php';

    $sql = 'SELECT *
            FROM books
            INNER JOIN genres
            ON books.genre_id = genres.genre_id';

    $books = $pdo->query($sql);

    ob_start();
    include 'templates/listbook.html.php';
    $output = ob_get_clean();
} catch (PDOException $e) {
    $title = 'An error has occured';
    $output = 'Database error: ' . $e->getMessage();
}
include 'templates/layout.html.php';
