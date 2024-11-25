<?php
try {
    if (isset($_POST['id'])) {
        include 'includes/DatabaseConnection.php';

        $sql = 'DELETE FROM joke WHERE id = :id';
        //prepare a statement
        $stm = $pdo->prepare($sql);
        // bind assign id value
        $stm->bindValue(':id', $_POST['id']);
        //execute(run) statement
        $stm->execute();
        //redirect
        header("Location: jokes.php");
    }
} catch (PDOException $error) {
    echo "Fail";
}
