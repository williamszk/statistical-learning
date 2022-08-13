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

const menuMovies = () => {
	menu({ add: addMovies, list: listMovies });
};

const menuTravels = () => {
	menu({ add: addTravels, list: listTravels });
};

const menu = (commandOptions) => {
	const prompt = require("prompt-sync")({ sigint: true });
	let userInput = prompt("What is your command? > ");

	while (true) {
		
		if (Object.keys(commandOptions).includes(userInput )) {
			commandOptions[userInput]()
		}
		if (userInput == "exit") {
			console.log("Good bye :)");
			break;
		}
		userInput = prompt("What is your command? > ");
	}
};


// menuMovies();
// menuTravels();

// Exercise: include also the options of:
// Books, Tourist Attractions


const addBooks = () => {
	console.log("Adding Books...");
};

const listBooks = () => {
	console.log("List all Books...");
};

const menuBooks = () => {
	menu({ add: addBooks, list: listBooks });
};

menuBooks();