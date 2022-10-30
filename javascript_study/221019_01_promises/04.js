const recordVideoOne = new Promise((resolve, reject) => {
	resolve("Video 1 Recorded");
});

const recordVideoTwo = new Promise((resolve, reject) => {
	resolve("Video 2 Recorded");
});

const recordVideoThree = new Promise((resolve, reject) => {
	resolve("Video 3 Recorded");
});

// wait for all Promise to return something
Promise.all([
	recordVideoOne,
	recordVideoTwo,
	recordVideoThree,
	// the message here is an array of resolve arguments
]).then((messages) => {
	console.log(messages);
});
// with this method we can run all three promises at the same time

// in the case of the method .race(), the output will be a single message
// it will return only the first Promise that finishes
Promise.race([
	recordVideoOne,
	recordVideoTwo,
	recordVideoThree,
]).then((message) => {
	console.log(message);
});