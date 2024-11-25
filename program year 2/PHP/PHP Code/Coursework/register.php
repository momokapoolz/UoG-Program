<?php
if (!isset($_POST['register'])) {
    include 'register.html.php';
} else {
    include './sql/connection.php';
    include './sql/dbfunction.php';

    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['passwordconfirm'];

    $encrypt = md5($password);
    $cf_encrypt = md5($confirm_password);

    if ($password != $confirm_password) {
        echo "Passwords do not match";
        header('Location: register.php');
    } else {
        /*$sql = "INSERT INTO user SET username = :username, password = :password, email = :email";
        $stm = $pdo->prepare($sql);
        $stm->bindValue(':username', $username);
        $stm->bindValue(':password', $password);
        $stm->bindValue(':email', $email);
        $stm->execute();*/
        register($pdo, $username, $encrypt , $email);
        //redirect to login
        header('location: login.php');
    }
}
