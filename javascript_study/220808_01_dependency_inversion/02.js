// Include menu functions

const addMovies = () => {
	console.log("Adding movies...");
};

const listMovies = () => {
	console.log("List all movies...");
};

const addTravels = () => {
	console.log("Adding Travels...");
};

const listTravels = () => {
	console.log("List all Travels...");
};

const menu = (product) => {
	const prompt = require("prompt-sync")({ sigint: true });
	let userInput = prompt("What is your command? > ");

	while (true) {
		if (userInput == "add") {
			switch (product) {
				case "Movies":
					addMovies();
					break;
				case "Travels":
					addTravels();
					break;
				default:
					break;
			}
		}
		if (userInput == "list") {
			switch (product) {
				case "Movies":
					listMovies();
					break;
				case "Travels":
					listTravels();
					break;
				default:
					break;
			}
		}

		if (userInput == "exit") {
			console.log("Good bye :)");
			break;
		}
		userInput = prompt("What is your command? > ");
	}
};

// menu("Movies");
menu("Travels");

// Exercise: include also the options of: 
// Books, Tourist Attractions