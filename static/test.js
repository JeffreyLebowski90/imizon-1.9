function show() {
  var x = document.getElementById("myDIV");
  x.style.display = "block";
}

function hide(){
	var x = document.getElementById("myDIV");
	x.style.display = "none";
}

function showShipping(divID){
	// var x = document.getElementById("FCA");
	// x.style.display = "block";
	document.getElementById("FCA").style.display = "none";
	document.getElementById("FOB").style.display = "none";
	document.getElementById("DDP").style.display = "none";
	document.getElementById(divID).style.display = "block";
}