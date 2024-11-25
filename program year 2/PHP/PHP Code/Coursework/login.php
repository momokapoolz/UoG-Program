<?php
try {
    //include 'connection.php';
    if (!isset($_POST['login'])) {
        include 'login.html.php';
    } else {
        include './sql/connection.php';
        include './sql/dbfunction.php';

        $username = $_POST['username'];
        $password = $_POST['password'];
        $encrypt = md5($password);

        /*$sql = "SELECT * FROM user WHERE username = :username AND password = :password";
        $stm = $pdo->prepare($sql);
        $stm->bindValue(':username', $username);
        $stm->bindValue(':password', $password);
        $stm->execute();
        $check = $stm->fetchAll();*/
        
        login($pdo, $username, $encrypt);
        $check = login($pdo, $username, $encrypt);


        $result = count($check);


        if ($result >= 1) {
            //start new session
            session_start();
            //create session variable to store username
            $_SESSION['username'] = $username;
            //redirect to homepage
            //Note: redirect the page based on role
            //Ex: user role => redirect to index.php
            //Ex: admin role => redirect to index_admin.php
            
            if ($username == 'admin' AND $password == 'admin') {
                header("Location: ./adminlayout/home.php");
            } else {
                header('Location: index.php');
            }
        }
        //2. case 2: user login failed
        else {
            echo `<script>
            window.location.href = "index.php"
            alert("Username or Password is incorrect")
            </script>`;
            header('Location: login.php');
        }
    }
} catch (PDOException $e) {
    $title = 'An error has occured';
    $output = 'Database error: ' . $e->getMessage();
}









//<?php
//check whether user has submitted login form or not
//1st case: NO => display form to user
/*if (!isset($_POST['login'])) {
    include 'login.html.php';
}
//2nd case: YES => process the form
else {
    //get input data from the form
    $username = $_POST['username'];
    $password = $_POST['password'];
    $encrypted = md5($password);  //encrypt password

    //connect to database
    include 'dbconnect.php';

    $sql = "SELECT * FROM user WHERE username = :username AND password = :password";
    //$sql = "SELECT * FROM user WHERE username = ? AND password = ?";
    $stm = $pdo->prepare($sql);
    $stm->bindValue(':username', $username);
    $stm->bindValue(':password', $encrypted);
    // $stm->bindParam(1, $username);
    // $stm->bindParam(2, $password);
    $stm->execute();
    $result = $stm->fetchAll();
    $total = count($result);
    // echo $total;

    if ($total >= 1) {
        //echo "login succeed !";
        //start session after success login
        session_start();
        $_SESSION['authorized'] = true;
        $_SESSION['username'] = $username;
        //redirect page
        header('Location: admin.php');
    } else {
        //echo "login failed !";
        header('Location: login.php');
    }
}*/
//
