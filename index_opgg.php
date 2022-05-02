<?php
$nick = $_GET['nick'];
exec("python3 index_opgg.py", $nick);
?>