<?php
/* case 1: user didn't enter information to Edit form
=> display the form first
*/
if (!isset($_POST['question_text'])) {
    try {
        include '../sql/connection.php';
        $sql = 'SELECT * FROM questions 
                WHERE id = :id';
        $statement = $pdo->prepare($sql);
        $statement->bindValue(':id', $_GET['id']);
        $statement->execute();
        $question = $statement->fetch();
        ob_start();
        include 'edit.html.php';
        $output = ob_get_clean();
        include 'layout.html.php';
    } catch (PDOException $e) {
        echo "DB error: $e";
    }
}

/*case 2: user already entered information to form
=> process the form => edit data in database
*/ else {
    try {
        include '../sql/connection.php';
        include '../sql/dbfunction.php';
        /*$sql = "UPDATE questions
                SET question_text = ?
                WHERE id = ?
            ";
        $statement = $pdo->prepare($sql);
        $statement->bindParam(1, $_POST['question_text']);
        $statement->bindParam(2, $_POST['id']);
        $statement->execute();*/
        edit_question($pdo, $_POST['question_text'], $_POST['id']);

        header("location: list.php");
    } catch (PDOException $e) {
        echo "DB error: $e";
    }
}
