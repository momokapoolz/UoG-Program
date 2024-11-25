<?php
// oput buffering start
ob_start();
//render web page
include 'contact.html.php';
//store content in output buffering then clean later
$content = ob_get_clean();
//render layout 
include 'layout.html.php';


?>