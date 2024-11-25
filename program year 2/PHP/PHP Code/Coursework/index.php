<?php
session_start();
ob_start();

//1st case: user did not login => show login form
if (!isset($_SESSION['username']))
    header('Location: login.php');

//2nd case: user already login => welcome page
else
    header('Location: ./userlayout/home.php');
