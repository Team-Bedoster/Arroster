<html lang="fr">
<head>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="css/css_system.css"/>
	<title>Arroz'oir - Paramètres du système</title>
	<link rel="icon" type="image/png" href="img/_icon.png"/>
	<script type="text/javascript" src="scripts/arrosageInstantane.js"></script>
	<script type="text/javascript" src="scripts/displaySettings.js"></script>
</head>


<body>

	<?php
		session_start();
		if(!isset($_SESSION['login']))
		{
			session_destroy();
			header("Location: index.php");
		}
		else{
			require_once('header.php');
		}
	?>
<div id="containerglobal">
	<fieldset id="glob">
		<fieldset id="instant2">
			<div id="arrosage_instantane" style="background-color: transparent">
				<img src="img/magnolia.jpg" style="max-width: 100%; max-height: 100%;">
			</div>
		</fieldset>

		<fieldset id="cond2">
			<form action='' method='POST'>
				<div id="arrosage_conditionnel">
					<h2>Magnolia Blanc</h2>
					<li>Température: 20 C°</li><br /><br />
					<li>Humidité pot: 68%</li><br /><br />
					<li>Date du relevé: 01/02/2019</li><br /><br />
					<br/>
				</div>

			</form>
		</fieldset>
	</fieldset>
</div>
<?php
require_once("footer.php");
?>
</body>
</html>
