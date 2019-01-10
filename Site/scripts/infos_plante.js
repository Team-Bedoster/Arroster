
window.onload = initPage;

function initPage() {


	let magnolia = new Image();
	magnolia.src = "https://bit.ly/2EBnS9j";

	let myosotis = new Image();
	myosotis.src = "https://bit.ly/2GwQPFI";

	let marigold = new Image();
	marigold.src = "https://bit.ly/2T23guS";


	var globalView = document.getElementById("global");

	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.name = 'plante';
	cadre.style.width = '20%';
	cadre.style.height = '20%';
	
	photo = document.createElement("img");
	photo.setAttribute('src', magnolia.src);
	photo.setAttribute('height', '100%');
	photo.setAttribute('width', '100%');
	photo.setAttribute('border-radius', '50%');
	photo.style.borderRadius = '30px';
	
	cadre.appendChild(photo);
	globalView.appendChild(cadre);

	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.name = 'plante';
	cadre.style.width= '20%';
	
	photo = document.createElement("img");
	photo.setAttribute('src', myosotis.src);
	photo.setAttribute('height', '100%');
	photo.setAttribute('width', '100%');
	photo.style.borderRadius = '30px';
	
	cadre.appendChild(photo);
	globalView.appendChild(cadre);

	
	cadre = document.createElement("div");
	cadre.id = 'cadre';
	cadre.name = 'plante';
	cadre.style.width= '20%';
	
	photo = document.createElement("img");
	photo.setAttribute('src', marigold.src);
	photo.setAttribute('height', '100%');
	photo.setAttribute('width', '100%');
	photo.style.borderRadius = '30px';
	
	cadre.appendChild(photo);
	globalView.appendChild(cadre);
	
	theFutureIsNow();
}












