<?php
require("database_settings.php");


$file = "data/login.csv";

if(isset($_POST['login'], $_POST['password']))
	{
	if(!empty($_POST['login']) and !empty($_POST['password']))
		{
		
		$login = $_POST['login'];
		$password = $_POST['password'];
		
		$pointeur = fopen($file, 'r');
		
		while(!feof($pointeur))
			{
			$t = fgetcsv($pointeur, 1024, ",");
			}
		
		
		if($login == $t[0] and $password == $t[1]){
			fclose($pointeur);
			session_start();
			$_SESSION['login'] = $login;
			$_SESSION['role'] = "admin";
			header('Location: overview.php');
		} else{
			header("Location: index.php?id=1");
			echo "<p> Le nom d'utilisateur ou le mot de passe n'existe pas dans notre base de données.</p>";
		}
		
	}		
}
?>