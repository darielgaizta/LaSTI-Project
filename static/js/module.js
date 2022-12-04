function toggleModule(id) {
	module = document.getElementById(id);
	if (module.style.display == "block") {
		module.style.display = "none";
	} else {
		module.style.display = "block";
	}
}