var ss=0;
var s=00;
var m='0'+0;

function startSpraying()
{
    var verifActif = document.getElementById("aiActif");
    if(verifActif.checked)
    {
        declenchement = new XMLHttpRequest();
        declenchement.onreadystatechange = callback_enregistre;
        declenchement.open("POST", "simuArrosage.php");
        declenchement.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        var requete = "arrose=" + true;
        declenchement.send(requete);

        launchTimer();
        document.getElementById("arroser").value = "Arrêter l'arrosage";
        document.getElementById("arroser").onclick = stopSpraying;
        document.getElementById("aiInactif").disabled = 1;
    }
}


function launchTimer()
{
    if (m==0) {m='00'}
    if (s<10){s='0'+s;}
    if (ss<10){ss='0'+ss;}
    level = document.getElementById("temps_arrosage").innerHTML = m + " minutes et " + s + " secondes" ;
    s++;
    ss++;
    if (s==60){s=0;s=0; m++;if(m<10){m='0'+m;}}
    if (m==60){m='0'+0;h++;if(h<10){h='0'+h;}}
    chrono = window.setTimeout("launchTimer();",1000);
}

function stopSpraying()
{
    window.clearTimeout(chrono);
    ss = 0;
    s = 00;
    m = '0'+0;
    document.getElementById("temps_arrosage").innerHTML = m + " minutes et " + s + " secondes" ;
    document.getElementById("arroser").value = "Arroser";
    document.getElementById("arroser").onclick = startSpraying;
    document.getElementById("aiInactif").disabled = 0;
}


function callback_enregistre()
{
    if(declenchement.readyState == 4 && declenchement.status == 200)
	{
		console.log("Ca marche");
	}
}
