<?php
if (isset($_POST['question_text'])) {
    try {
        include '../sql/connection.php';
        include '../sql/dbfunction.php';

        /*$sql = 'INSERT INTO questions SET
                question_text = :question_text,
                question_date = CURDATE()';
        $stmt = $pdo->prepare($sql);
        $stmt->bindValue(':question_text', $_POST['question_text']);
        $stmt->execute();*/

        insert_question($pdo, $_POST['question_text'], $_FILES['fileToUpload']['name'], $_POST['userid']);

        include '../sql/uploadFile.php';
        header('location: list.php');
    } catch (PDOException $e) {
        $title = 'An error has occurred';
        $output = 'Database error: ' . $e->getMessage();
    }
} else {
    $title = 'Post new question';
    ob_start();
    try {
        include '../sql/connection.php';
        $sql = "SELECT * FROM user";
        $user = $pdo->query($sql);
        include 'insert.html.php';
        $output = ob_get_clean();
    } catch (PDOException $e) {
        echo "Error : $e";
    }
}
include 'layout.html.php';