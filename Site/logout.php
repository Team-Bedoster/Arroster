<?php
session_start();
session_destroy();
unset($_SESSION["nom"]);
header('Location: index.php');
?>