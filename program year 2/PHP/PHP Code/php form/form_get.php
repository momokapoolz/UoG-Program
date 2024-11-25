<?php

$name = $_GET['name'];
$age = $_GET['age'];
$mom = $_GET['mom'];

echo htmlspecialchars("Ten may: " . $name, ENT_QUOTES);
echo "\t";
echo "Tuoi may: " . $age;
echo "\t";
echo "Me may: " . $mom;
echo "\t";
?>