<?php
$enArrosage = $_POST['arrose'];

/* SCRIPT DE TESTS - Création d'un fichier qui contient la date
On vérifie que l'activation de l'arrosage instantané produit une action

if($enArrosage == true)
{
    $thedate=date("D d F - H:i");
    $file="ladate.txt";

    if (file_exists($file)){
 $pointeur=fopen($file,"a");
 fputs($pointeur,"\n".$thedate);
 fclose($pointeur);
} else {
 $pointeur=fopen($file,"w");
 fputs($pointeur,$thedate);
 fclose($pointeur);
}
echo "Affichage ";

$i=0;
$pointeur=fopen($file,"r");
while (!feof($pointeur))
{
$t=fgets($pointeur,1024);
echo "Ligne : ".$i." => ".$t."<br>";
$i++;
}
}
else
{
    echo "bon";
}*/
 ?>
