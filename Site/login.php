<?php
require("database_settings.php");

$bd="myspraying"; 
$table="users";


if(isset($_POST['login'], $_POST['password']))
{
	if(!empty($_POST['login']) and !empty($_POST['password']))
	{
		$connexion=mysqli_connect($server,$login,$password)
		or die("Connexion impossible au serveur $server pour $login");

		mysqli_select_db($connexion,$bd)
		or die("Impossible d'accèder à la base de données");

		$requete="SELECT * FROM $table ORDER BY id";
		$resultat=mysqli_query($connexion,$requete);

		$username = $_POST['login'];
		$pass = $_POST['password'];
		while($row = mysqli_fetch_row($resultat))
		{
			if($username == $row[1] and $pass = $row[2])
			{
				session_start();
				$_SESSION["nom"] = $_POST['login'];
				mysqli_close($connexion);
				header('Location: intranet.php');
			}
			else
			{
				mysqli_close($connexion);
				header("Location: index.php?id=1");
			}
		}
		
		
	}
	
}
?>