<?php
setcookie("city", "tokyo", time() + 1000000);
?>

<h2><?=$_COOKIE['city']?></h2>