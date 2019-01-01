<?php
$enArrosage = $_POST['arrose'];

/* SCRIPT DE TESTS - Création d'un fichier qui contient la date
On vérifie que l'activation de l'arrosage instantané produit une action
*/

$file="test_simu_arrosage.txt";

if (file_exists($file))
{
    $pointeur=fopen($file,"a");
    if($enArrosage == true)
    {
        fputs($pointeur,"\nmarche");
    }
    else
    {
        fputs($pointeur, "\narrêt");
    }

    fclose($pointeur);
}
else
{
    $pointeur=fopen($file,"w");
    if($enArrosage == true)
    {
        fputs($pointeur,"marche");
    }
    else
    {
        fputs($pointeur, "arrêt");
    }

    fclose($pointeur);
}
exit(0);
 ?>
