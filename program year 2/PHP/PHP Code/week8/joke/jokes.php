<?php
try{
    include 'includes/DatabaseConnection.php';
    include 'includes/DatabaseFunction.php';

    $sql = 'SELECT joke.id, joketext, `name`, email, categoryName FROM joke
    INNER JOIN author ON authorid = author.id
    INNER JOIN category ON categoryid = category.id';

    $jokes = $pdo->query($sql);
    $title = 'Joke list';

    $totalJoke = totalJokes($pdo);
    $totalAuthor = totalAuthors($pdo);

    ob_start();
    include 'templates/jokes.html.php';
    $output = ob_get_clean();
}catch (PDOException $e){
    $title = 'An error has occured';
    $output= 'Database error: ' . $e->getMessage();
}
include 'templates/layout.html.php';