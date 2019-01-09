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
		<div id="planteG">
		</div>
		
		<img id="planteD">
		
		
		<fieldset id="instant">
			<div id="arrosage_instantane">
				<h2>Arrosage instantané</h2>
				<!--ai = arrosage instantané-->
				<input id="aiActif" type="radio" value="Actif" name="arrosage_instantane" required/><label>Actif</label>
				<br>
				<input id="aiInactif" type="radio" name="arrosage_instantane" value="Inactif"><label>Inactif</label>
				<p>Temps d'arrosage: </p><p id="temps_arrosage"></p>
				<input id="arroser" onclick="startSpraying();" type="button" name="lancement_arrosage" value="Arroser">
			</div>
		</fieldset>

		<fieldset id="cond">
			<form action='' method='POST'>
				<div id="arrosage_conditionnel">
					<h2>Arrosage conditionnel</h2>
					<input id="acActif" type="radio" value="Actif" name="arrosage_conditionnel" required/><label>Actif</label>
					<br/></br>
					<input id="acInactif" type="radio" value="Inactif" name="arrosage_conditionnel" required/><label>Inactif</label>
					<br/>
				</div>


				<div id="pac"><!--pac = Paramètres Arrosage Conditionnel-->
					<h2>Paramètres</h2>
					<h3>Fréquence de tests:</h3>
					<input type="text" name="frequence_tests" id="frequence_tests">
					<select name="uft" id="uft"><!--uft = unité de fréquence de tests (c-à-d minutes ou heures)-->
						<option>minutes</option>
						<option>heures</option>
					</select>

					<h3>Conditions d'arrosage</h3>
					<p><label>Taux d'humidité: </label><input type="text" name="humidite" id="humidite"> %</p>

					<h3>Fréquence d'arrosage:</h3>
					<input type="text" name="frequence_arrosage" id="frequence_arrosage">
					<select id="ufa" name="ufa"><!--ufa = unité de fréquence d'arrosage (c-à-d minutes ou heures)-->
						<option>minutes</option>
						<option>heures</option>
					</select>
				</div>

				<input id="valider" type="submit" name="valider" value="Valider">
			</form>
		</fieldset>
	</fieldset>
</div>
<?php
require_once("footer.php");
?>
</body>
</html>
