const userLeft = false;
const userWatchingCatMeme = false;

function watchTutorialPromise() {
	return new Promise((resolve, reject) => {
		// can also do a lot of stuff that takes IO time
		// in this part

		if (userLeft) {
			reject({
				name: "User left",
				message: "sad face :(",
			});
		} else if (userWatchingCatMeme) {
			reject({
				name: "User watching cat meme",
				message: "WebDevSimplified < Cat",
			});
		} else {
			resolve("Thumbs up and Subscribe");
		}
	});
}

const myPromise = watchTutorialPromise();

// can do other stuff in this part
// that uses CPU

// in here js needs to wait for the
myPromise
	.then((message) => {
		console.log("Success: " + message);
	})
	.catch((error) => {
		console.log(error.name + " - " + error.message);
	});
