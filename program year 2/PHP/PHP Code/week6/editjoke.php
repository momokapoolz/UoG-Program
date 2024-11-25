<?php
if (!isset($_POST['joketext'])) {
    try {
        include 'includes/DatabaseConnection.php';
        $id = $_GET['id'];
        $sql = 'SELECT * FROM joke
                WHERE id = :id';
        $stm = $pdo->prepare($sql);
        $stm->bindValue(':id', $id);        
        $stm->execute();
        $joke = $stm->fetch();
        ob_start();
        include 'templates/editjoke.html.php';
        $output = ob_get_clean();
        include 'templates/layout.html.php';
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}

else {
    try {
        include 'includes/DatabaseConnection.php';
        $sql = 'UPDATE joke
                SET joketext = ?
                WHERE id = ?';
        
        $stm = $pdo->prepare($sql);
        $stm->bindParam(1, $_POST['joketext']);
        $stm->bindParam(2, $_POST['id']);
        $stm->execute();
        header("location: jokes.php");
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
    
}
