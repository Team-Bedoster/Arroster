<?php
	session_start();
?>

<html lang="fr">
<head>
	<title></title>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="home_style.css"/>
	<script src="scripts/infos_plante.js" type="text/javascript" > </script>
</head>
<body>
	<h1>Aperçu Général</h1>
	<fieldset>
		
	</fieldset>



<?php
	require "externals/simple_html_dom/simple_html_dom.php";
    $search_query = "Plante verte";
    $search_query = urlencode( $search_query );
    $html = file_get_html("https://www.google.com/search?client=firefox-b-ab&biw=1920&bih=903&tbm=isch&sa=1&ei=X3oXXI-TB4Scaai0urAI&q=plante+verte&oq=plante+verte&gs_l=img.3.0.35i39l2j0l5j0i30l3.1100.1256..1587...0.0..0.124.237.0j2......1....1..gws-wiz-img.EpH2qOC2SMk");
	$image_count = 100; //Enter the amount of images to be shown
	$tableau = Array();
	$i = 0;
	for($i=0; $i<100; $i++){
		array_push($tableau, $html->find('img', $i));
		echo $html->find('img', $i);
		$i++;
	}
	//echo $tableau;
?>