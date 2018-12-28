window.onload = initSettings

function initSettings()
{
    //Test pour l'arrosage Instantané (ai $ arrosage instantané)
    aiActif = document.getElementById("aiActif");
    aiActif.onchange = settings;
    aiInactif = document.getElementById("aiInactif");
    aiInactif.onchange = settings;
}

function settings()
{
    if(aiInactif.checked)
    {
        document.getElementById("arroser").disabled = 1;
        document.getElementById("ai").disabled = 0;
        document.getElementById("ac").disabled = 0;
        document.getElementById("frequence_tests").disabled = 0;
        document.getElementById("uft").disabled = 0;
        document.getElementById("frequence_arrosage").disabled = 0;
        document.getElementById("ufa").disabled = 0;
        document.getElementById("humidite").disabled = 0;
        document.getElementById("valider").disabled = 0;
    }
    else
    {
        document.getElementById("arroser").disabled = 0;
        document.getElementById("ai").disabled = 1;
        document.getElementById("ac").disabled = 1;
        document.getElementById("frequence_tests").disabled = 1;
        document.getElementById("uft").disabled = 1;
        document.getElementById("frequence_arrosage").disabled = 1;
        document.getElementById("ufa").disabled = 1;
        document.getElementById("humidite").disabled = 1;
        document.getElementById("valider").disabled = 1;


    }
}
