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

<div>
    <a id="home" href=""><h1 id="titre">Arroz'oir</h1></a>
		<nav id="menu">
			<ul id="menu-links">
				<li><a title="Accueil" href="">Accueil</a></li>
                <li>&#124;</li>
				<li><a title="États des plantes" href="states.php">États des plantes</a></p></li>
				<li>&#124;</li>
				<li><a title="Paramètres du système" href="system_settings.php">Paramètres du système</a></li>
                <li>&#124;</li>
                <a href='logout.php'>Déconnexion</a>
			</ul>
		</nav>
</div>
