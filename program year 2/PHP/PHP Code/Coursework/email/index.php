<?php
if (!isset($_POST['send'])) {
    include 'phpmailer.html.php';
} else {
    $subject = $_POST['subject-body'];
    $body = $_POST['email-body'];
    include 'phpmailer.php';
}

?>