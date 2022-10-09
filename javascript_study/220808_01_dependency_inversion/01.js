const addMovies = () => {
	console.log("Adding movies...");
};

const listMovies = () => {
	console.log("List all movies...");
};

const menuMovies = () => {
	const prompt = require("prompt-sync")({ sigint: true });
	let userInput = prompt("What is your command? > ");

	while (true) {
		if (userInput == "add") addMovies();
		if (userInput == "list") listMovies();
		if (userInput == "exit") {
			console.log("Good bye :)");
			break;
		}

		userInput = prompt("What is your command? > ");
	}
};

const addTravels = () => {
	console.log("Adding Travels...");
};

const listTravels = () => {
	console.log("List all Travels...");
};

const menuTravels = () => {
	const prompt = require("prompt-sync")({ sigint: true });
	let userInput = prompt("What is your command? > ");

	while (true) {
		if (userInput == "add") addTravels();
		if (userInput == "list") listTravels();
		if (userInput == "exit") {
			console.log("Good bye :)");
			break;
		}

		userInput = prompt("What is your command? > ");
	}
};

// menuMovies();
menuTravels();
// Exercise: include also the options of: 
// Books, Tourist Attractions

