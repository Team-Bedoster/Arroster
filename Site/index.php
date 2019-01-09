<html lang="fr">
<head>
	<title>Arroz'oir - Connexion</title>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="css/css_formulaire.css"/>
</head>
<body>
	<div id="formulaire">
	
		<h1>Connexion</h1>


		<form action='login.php' method='POST'>
		
			<label>Nom d'utilisateur:</label><input type="text" name="login" required/>
			<br/>
			<label>Mot de passe:</label><input type="password" name="password" required/>
			<br/>
			<input type="submit" value="Login" />
		
		</form>
	
	</div>

	
<?php

session_start();
if(isset($_SESSION["login"]))
	{
	header("Location: overview.php");
	}
else
	{
	session_destroy();
	}
if(isset($_GET["id"]))
	{
	echo "<div class='icon-bar'>
				<i class='active'></i>
				<input type='submit' value='Connexion impossible' class='pdf'>
				</div>";
	}
	
?>


</body>
</html>
