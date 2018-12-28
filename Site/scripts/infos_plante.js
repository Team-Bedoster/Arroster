
window.onload = initPage;

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


}
