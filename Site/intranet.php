<?php
session_start();
echo "<h1>Intranet</h1>";
if(!isset($_SESSION["nom"]))
{
	session_destroy();
	header("Location: index.php");
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
	<title></title>
	<meta charset="utf-8"/>
	<link rel="stylesheet" href="intranet_style.css"/>
</head>
<body>
<form action='logout.php' method='POST'>
<input name="logout" type="submit" value="Déconnexion" />
</form>
</html>