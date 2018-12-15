<html lang="fr">
<head>
	<title></title>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="home_style.css"/>
</head>
<body>
	<h1>Connexion</h1>
	<fieldset>
	<form action='login.php' method='POST'>
		<label>Nom d'utilisateur:</label><input type="text" name="login" required/>
		<br/>
		<label>Mot de passe:</label><input type="password" name="password" required/>
		<br/>
		<input type="submit" value="Connexion" />
	</form>
	</fieldset>

<?php
session_start();
if(isset($_SESSION["user"]) and !empty($_SESSION["user"]))
{
	header("Location: intranet.php");
}
else
{
	session_destroy();
}
if(isset($_GET['id']))
{
	echo "<p> Le nom d'utilisateur ou le mot de passe n'existe pas dans notre base de données.</p>";
}
?>
</body>
</html>