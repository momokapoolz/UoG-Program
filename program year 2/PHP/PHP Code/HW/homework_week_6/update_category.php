<?php
if (!isset($_POST['category'])) {
    try {
        $pdo = new PDO('mysql:host=localhost; dbname=week6_db; charset=utf8mb4','root', '');
        $id = $_GET['id'];
        $sql = 'SELECT * FROM category
                WHERE id = :id';
        $stm = $pdo->prepare($sql);
        $stm->bindValue(':id', $id);        
        $stm->execute();
        $category = $stm->fetch();
        ob_start();
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}

else {
    try {
        $pdo = new PDO('mysql:host=localhost; dbname=week6_db; charset=utf8mb4','root', '');
        $sql = 'UPDATE category
                SET category = ?
                WHERE id = ?';
        
        $stm = $pdo->prepare($sql);
        $stm->bindParam(1, $_POST['category']);
        $stm->bindParam(2, $_POST['id']);
        $stm->execute();
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
    
}

include 'update_category.html.php';
?>