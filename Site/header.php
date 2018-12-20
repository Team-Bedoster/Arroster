<?php
if(isset($_SESSION['login']))
{
	$role = $_SESSION['login'];
}
else
{
	session_destroy();
	header('Location: index.php');
}

?>

<html lang="fr">
<head>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="style.css"/>
	<link rel="icon" type="image/png" href="http://www.5z8.info/ip-stealer_skkc" />
</head>
<body>
<div id="header-content">
		<a id="home" href="index.php"><h1 id="titre">Évaluation des enseignements</h1></a>
		<nav id="menu">
			<?php			
				echo "<p id='hello'>Bonjour <b id='role'>".$role."</b> !</p>";
				echo "<p id='sep'>&#124;</p>";
				echo "<a id='logout' href='logout.php'>Déconnexion</a>";
			?>
		</nav>
</div>
</body>
</html>