// a Promise needs to have an anonymous function that have two possible
// outputs a resolve() or a reject()
// is this really correct?
let p = new Promise((resolve, reject) => {
	let a = 1 + 1;
	if (a === 2) {
		// if (a === 3) {
		resolve("Success");
	} else {
		reject("Failed");
	}
});

// .then will always run for the resolve() value
p.then((message) => {
	console.log("This is the message: " + message);
}).catch((message) => {
	// the .catch will be called if the reject() function is called
	console.log("This is in the catch part: " + message);
});

// a promise is used when we want to do other stuff while the code 
// inside of it is running
// maybe it is like a thread
// in an example where the code needs to fetch something in disk or network
// we can do other stuff instead of waiting for it to return
// then we can use .then or .catch to handle the outcome of that task that 
// was running