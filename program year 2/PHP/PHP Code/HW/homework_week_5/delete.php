<?php
try {
    if (isset($_POST['id'])) {
        include 'connectsql.php';

        $sql = 'DELETE FROM employee WHERE id = :id';
        //prepare a statement
        $stm = $pdo->prepare($sql);
        // bind assign id value
        $stm->bindValue(':id', $_POST['id']);
        //execute(run) statement
        $stm->execute();
        //redirect
        header("Location: view.php");
    }
} catch (PDOException $error) {
    echo "Fail";
}
