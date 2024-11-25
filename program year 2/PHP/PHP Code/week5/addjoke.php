<?php
if (!isset($_POST['text'])) {
    ob_start();
    include 'templates/addjoke.html.php';
    $output = ob_get_clean();
    include 'templates/layout.html.php';
}
else {
    try {
        include 'includes/DatabaseConnection.php';

        $sql = 'INSERT INTO joke(joketext, jokedate) VALUES (:joketext, :jokedate)';

        $stm = $pdo->prepare($sql);
        $stm->bindValue(':joketext', $_POST['text']);
        $stm->bindValue(':jokedate', $_POST['date']);
        $stm->execute();

        header('location: jokes.php');
    } catch (PDOException $ex) {
        echo "Fail" + $ex;
    }
}
?>