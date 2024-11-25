<?php
if (!isset($_POST['first_name'])) {
    ob_start();
    include 'insert.html.php';
    $output = ob_get_clean();
    include 'layout.html.php';
}
else {
    try {
        include 'connectsql.php';

        $sql = 'INSERT INTO employee(first_name, last_name, email) VALUES (:first_name, :last_name, :email)';

        $stm = $pdo->prepare($sql);
        $stm->bindValue(':first_name', $_POST['first_name']);
        $stm->bindValue(':last_name', $_POST['last_name']);
        $stm->bindValue(':email', $_POST['email']);
        $stm->execute();

        header('location: view.php');
    } catch (PDOException $ex) {
        echo "Fail" + $ex;
    }
}

?>