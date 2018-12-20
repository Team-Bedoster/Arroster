
window.onload = initPage;


function event_handler(){
	document.getElementById("cadre").onfocus = requeteEnregistrement;
	
}

function requeteEnregistrement(){
	var leClic = new XMLHttpRequest();
	leClic.open("POST", "Voiliers_enregistrer.php", true);
	leClic.setRequestHeader("Content-Type", "application/x-www-form-encoded");
	var form = document.forms.bob;
	var params;
	for(i=0; i<form.length-1; i++){
		params += form[i].name + "=" + form[i].value + "&";
	}
	leClic.send(params);
	
	
	
}

function callback_Enregistrement(){
	if(leClic.readyState==4 && leClic.status==200){
		
	}
}


function initPage() {
	
	let magnolia = new Image();
	magnolia.src = "https://bit.ly/2EBnS9j";
	magnolia.style.width= '12%';
	
	let myosotis = new Image();
	myosotis.src = "https://bit.ly/2GwQPFI";
	
	let marigold = new Image();
	marigold.src = "https://bit.ly/2T23guS";
	
	
	var globalView = document.getElementById("global");
	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.style.width= '12%';
	cadre.appendChild(magnolia);
	globalView.appendChild(cadre);
	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.style.width= '12%';
	cadre.appendChild(myosotis);
	globalView.appendChild(cadre);
	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.style.width= '12%';
	cadre.appendChild(marigold);
	globalView.appendChild(cadre);
	
	
	
	
	xhrAfficheChoix = new XMLHttpRequest();
	xhrAfficheChoix.onreadystatechange = callback_afficheChoix;
	xhrAfficheChoix.open("GET", "voiliers.xml");
	xhrAfficheChoix.send();
	
	

}
function afficheSelection ()	{
	// indice = document.getElementById("choix").selectedIndex ;
	// descVoilier = xhr
	// nomVoilier = document.getElementById("choix").value ;
	// document.getElementById("selection").appendChild ( document.createTextNode (indice + 1 + " - " + nomVoilier));
		 
 
} //afficheSelection ()

function callback_peupleChoix(url){
	if(xhrPeupleChoix.readyState==4 && xhrPeupleChoix.status==200){
		tabNoms = xhrPeupleChoix.responseXML.getElementsByTagName("nom");
		for(var i=0; i<tabNoms.length; i++){
			nomVoilier = tabNoms[i].firstChild.nodeValue;
			leSelect = document.getElementById("choix");
			noeudOption = document.createElement("option");
			noeudTexte = document.createTextNode(nomVoilier);
			noeudOption.appendChild(noeudTexte);
			leSelect.appendChild(noeudOption);
		}
	}
}


function callback_afficheChoix(url){
	if(xhrAfficheChoix.readyState==4 && xhrAfficheChoix.status==200){
		clearContent(document.getElementById("selection"));
		
		indice = document.getElementById("choix").selectedIndex;
		
		voilier = xhrAfficheChoix.responseXML.getElementsByTagName("voilier")[indice];
		
		nom = xhrAfficheChoix.responseXML.getElementsByTagName("nom")[indice].firstChild.nodeValue;
		
		annee = xhrAfficheChoix.responseXML.getElementsByTagName("annee")[indice].firstChild.nodeValue;
		
		architecte = xhrAfficheChoix.responseXML.getElementsByTagName("architecte")[indice].firstChild.nodeValue;
		
		skipper = xhrAfficheChoix.responseXML.getElementsByTagName("nom_skipper")[indice].firstChild.nodeValue;
		
		texte = xhrAfficheChoix.responseXML.getElementsByTagName("texte")[indice].firstChild.nodeValue;
		
		photoAdresse = voilier.getElementsByTagName("photo")[0].getAttribute("adresse");
		photo = new Image();
		photo.src = photoAdresse;
		
		tabVoilier = [photo, nom, annee, architecte, skipper, texte];
		
		
		table = document.createElement("table");
		table.border="1";
		table.width="75%";
		tBody = document.createElement("TBODY");
		table.appendChild(tBody);

		
		for (var i = 0; i < 6; i++){
			var tr = document.createElement('tr');
			tBody.appendChild(tr);
			var td = document.createElement('td');
			td.width = '75';
			if(i==0)
				td.appendChild(photo);
			else
				td.appendChild(document.createTextNode(tabVoilier[i]));
			tr.appendChild(td);
		}
		
		
		document.getElementById("selection").appendChild(table);	
	}
}
	 

function clearContent(element){
	while(element.childNodes.length != 0)
		element.removeChild(element.childNodes[0]);
}


