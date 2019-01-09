<?php
if(isset($_SESSION['login']))
{
}
else
{
	session_destroy();
	header('Location: index.php');
}
?>


<head>
<html lang="fr">
<html>
<meta charset="UTF-8">
<link rel="stylesheet" href="css/css_header.css"/>

</head>
<div id = "container">
	
	<div id="headerarea">
	
		<div id="logo">
		<a href="/Arroster-web/Site/header.php">
			<img src = "img/logo.png" >
		</a>
		</div>
    
		<div id="search">
			<form class = "s" method="post" name="headerseach">
				<input id="searchtext" type="text" placeholder=" Rechercher..." >
				<input id="boutonsearch" type="image" src="img/bouton.png" onClick="clickit(this);">
					
			</form>
		</div>
	
	
		
		<nav id="menu">
			<ul id="menu-links">
				<li><a title="Accueil" href="overview.php">Accueil</a></li>
				<li>&#124;</li>
				<li><a title="États des plantes" href="overview.php">États des plantes</a></p></li>
				<li>&#124;</li>
				<li><a title="Paramètres du système" href="system_settings.php">Paramètres du système</a></li>
				<li>&#124;</li>
				<li><a href='logout.php'>Déconnexion</a></li>
			</ul>
		</nav>
		
	</div>
</div>




<body>















<footer>



<h2>&copy;</h2>
<p> Arroz'oir</p>



</footer>






</body>
</html>