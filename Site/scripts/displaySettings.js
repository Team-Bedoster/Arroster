window.onload = initSettings

function initSettings()
{
    //Test pour l'arrosage Instantané (ai $ arrosage instantané)
    aiActif = document.getElementById("aiActif");
    aiActif.onchange = settings;
    aiInactif = document.getElementById("aiInactif");
    aiInactif.onchange = settings;

    acActif = document.getElementById("acActif");
    acActif.onchange = settings;
    acInactif = document.getElementById("acInactif");
    acInactif.onchange = settings;
}

function settings()
{
    if(aiActif.checked)
    {
        document.getElementById("arroser").disabled = 0;
        document.getElementById("acActif").disabled = 1;
        document.getElementById("acInactif").disabled = 1;
        document.getElementById("frequence_tests").disabled = 1;
        document.getElementById("uft").disabled = 1;
        document.getElementById("frequence_arrosage").disabled = 1;
        document.getElementById("ufa").disabled = 1;
        document.getElementById("humidite").disabled = 1;
        document.getElementById("valider").disabled = 1;

    }
    else if(aiInactif.checked)
    {
        document.getElementById("arroser").disabled = 1;
        document.getElementById("acActif").disabled = 0;
        document.getElementById("acInactif").disabled = 0;
        document.getElementById("frequence_tests").disabled = 0;
        document.getElementById("uft").disabled = 0;
        document.getElementById("frequence_arrosage").disabled = 0;
        document.getElementById("ufa").disabled = 0;
        document.getElementById("humidite").disabled = 0;
        document.getElementById("valider").disabled = 0;
    }

    if(acActif.checked)
    {
        console.log(".");
        document.getElementById("aiActif").disabled = 1;
        document.getElementById("aiInactif").disabled = 1;
        document.getElementById("arroser").disabled = 1;
        document.getElementById("frequence_tests").disabled = 0;
        document.getElementById("uft").disabled = 0;
        document.getElementById("frequence_arrosage").disabled = 0;
        document.getElementById("ufa").disabled = 0;
        document.getElementById("humidite").disabled = 0;
    }
    else if(acInactif.checked && !aiInactif.checked)
    {
        document.getElementById("aiActif").disabled = 0;
        document.getElementById("aiInactif").disabled = 0;
        document.getElementById("arroser").disabled = 0;
        document.getElementById("frequence_tests").disabled = 1;
        document.getElementById("uft").disabled = 1;
        document.getElementById("frequence_arrosage").disabled = 1;
        document.getElementById("ufa").disabled = 1;
        document.getElementById("humidite").disabled = 1;
    }

}
