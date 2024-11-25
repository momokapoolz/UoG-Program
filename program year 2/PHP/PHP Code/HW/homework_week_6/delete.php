<?php
try {
    if (isset($_POST['id'])) {
        $pdo = new PDO('mysql:host=localhost; dbname=week6_db; charset=utf8mb4','root', '');

        $sql = 'DELETE FROM category WHERE id = :id';
        //prepare a statement
        $stm = $pdo->prepare($sql);
        // bind assign id value
        $stm->bindValue(':id', $_POST['id']);
        //execute(run) statement
        $stm->execute();
        //redirect

        $sql1 = 'DELETE FROM product WHERE id = :id';
        //prepare a statement
        $stm1 = $pdo->prepare($sql1);
        // bind assign id value
        $stm1->bindValue(':id', $_POST['id']);
        //execute(run) statement
        $stm1->execute();


        header("Location: view_category.php");
    }
} catch (PDOException $error) {
    echo "Fail";
}
