<?php
include 'includes/DatabaseConnection.php';

function query($pdo, $sql, $parameters = []){
    $query = $pdo->prepare($sql);
    $query->execute($parameters);
    return $query;
}

function totalJokes($pdo){
    $query = $pdo->prepare('SELECT COUNT(*) FROM joke');
    $query->execute();
    $row = $query->fetch();
    return $row[0];
}

function totalAuthors($pdo){
    $query = $pdo->prepare('SELECT COUNT(*) FROM author');
    $query->execute();
    $row = $query->fetch();
    return $row[0];
}

function getJoke($pdo, $id){
    $parameters = [':id' => $id];
    $query = query($pdo, 'SELECT * FROM joke WHERE id = :id', $parameters);
    return $query->fetch();
}

function deleteJoke($pdo, $id){
    $parameters = [':id' => $id];
    $query = 'DELETE FROM joke WHERE id = :id';
    query($pdo, $query, $parameters);
}

function updateJoke($pdo, $jokeid, $joketext){
    $parameters = [':joketext' => $joketext, ':id' => $jokeid];
    $query = 'UPDATE joke SET joketext = :joketext WHERE id = :id';
    query($pdo, $query, $parameters);
}




?>