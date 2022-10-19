const userLeft = false;
const userWatchingCatMeme = true;

function watchTutorialCallback(callback, errorCallback) {
	if (userLeft) {
		errorCallback({
			name: "User left",
			message: "sad face :(",
		});
	} else if (userWatchingCatMeme) {
		errorCallback({
			name: "User watching cat meme",
			message: "WebDevSimplified < Cat",
		});
	} else {
		callback("Thumbs up and Subscribe");
	}
}

watchTutorialCallback(
	(message) => {
		console.log("Success: " + message);
	},
	(error) => {
		console.log(error.name + " - " + error.message);
	}
);

// We could use Promise to create the same functionality
// Promise was created for this situation.
// What is the advantage of using Promise? it is asynchronous 
// we can do other stuff while some other stuff runs in the background
// Check script 03.js