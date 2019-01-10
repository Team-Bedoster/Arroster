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

<html lang="fr">
<head>
	<title>Arroz'oir - États des plantes	</title>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="css/overview.css"/>
	<link rel="icon" type="image/png" href="img/_icon.png"/>
	<script src="scripts/infos_plante.js" type="text/javascript" ></script>
</head>
<body>
	<div id="global">
			<!--
				// require "externals/simple_html_dom/simple_html_dom.php";
				// $search_query = "plante verte";
				// $search_query = urlencode( $search_query );
				// $html = file_get_html("https://www.google.fr/search?q={$search_query}&tbm=isch");
				// $tableau = Array();
				// $i = 0;
				// foreach($html->find('img') as $element){
					// array_push($tableau, $element);
					// //echo $element. '<br>';
				// }
				// echo $tableau[mt_rand(0, sizeof($tableau) -1)];
			// ?>
			-->
	</div>
</body>
<?php
require_once('footer.php');