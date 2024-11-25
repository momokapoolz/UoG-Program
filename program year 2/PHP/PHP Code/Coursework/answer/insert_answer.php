<?php
if (isset($_POST['answer_text'])) {
    try {
        include '../sql/connection.php';
        include '../sql/dbfunction.php';

        /*$sql = 'INSERT INTO questions SET
                question_text = :question_text,
                question_date = CURDATE()';
        $stmt = $pdo->prepare($sql);
        $stmt->bindValue(':question_text', $_POST['question_text']);
        $stmt->execute();*/

        insert_answer($pdo, $_POST['answer_text'], $_POST['id']);

        
        header('location: ../userlayout/list.php');
    } catch (PDOException $e) {
        $title = 'An error has occurred';
        $output = 'Database error: ' . $e->getMessage();
    }
} else {
    $title = 'Post new answer';
    ob_start();
    try {
        include '../sql/connection.php';
        $sql = "SELECT * FROM questions";
        $user = $pdo->query($sql);
        include 'insert_answer.html.php';
        $output = ob_get_clean();
    } catch (PDOException $e) {
        echo "Error : $e";
    }
}
include '../userlayout/layout.html.php';