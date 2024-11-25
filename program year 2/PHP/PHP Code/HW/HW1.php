<?php

$a; $b; $c;
$x;
$phuong_trinh = ($a * ($x * $x)) + ($b * $x) + $c;


function solveQuadratic($a, $b, $c){
    $delta = ($b*$b) - (4 * $a *$c);
    if ($delta < 0){
        $result = "Vo Nghiem";
        return $result;
    }
    elseif($delta = 0){
        $result = -$b / 2 * $a;
        return $result;
    }
    else{
        $x1 = (-$b - sqrt($delta)) / 2 * $a;
        $x2 = (-$b + sqrt($delta)) / 2 * $a;
        return $x1; $x2;
    }
}


$test1 = solveQuadratic(1, 2, 3);
echo $test1;
echo "\n";
$test2 = solveQuadratic(3, 4, 5);
echo $test2;
?>