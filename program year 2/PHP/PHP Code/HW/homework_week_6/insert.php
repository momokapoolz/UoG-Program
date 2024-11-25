<?php

$pdo = new PDO('mysql:host=localhost; dbname=week6_db; charset=utf8mb4', 'root', '');

$sql = 'INSERT INTO category(category) VALUES (:category)';
$sql1 = 'INSERT INTO product(product_name, product_quantity, product_price, product_brand, product_image) VALUES (:product_name, :product_quantity, :product_price, :product_brand, :product_image)';

$stm = $pdo->prepare($sql);
$stm->bindValue(':category', $_POST['category']);
$stm->execute();

$stm1 = $pdo->prepare($sql1);
$stm1->bindValue(':product_name', $_POST['product_name']);
$stm1->bindValue(':product_quantity', $_POST['product_quantity']);
$stm1->bindValue(':product_price', $_POST['product_brand']);
$stm1->bindValue(':product_brand', $_POST['product_brand']);
$stm1->bindValue(':product_image', $_POST['product_image']);
$stm1->execute();




include 'insert.html.php';
