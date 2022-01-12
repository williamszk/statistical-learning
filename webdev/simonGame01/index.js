// use jQuery to make the game work

// array of color used in other places
var colorArray = ["blue", "red", "yellow", "green"];
var colorInterfaceButtons = ["green", "red", "yellow"];

var colorMaping = {
	blue: 0,
	red: 1,
	yellow: 2,
	green: 3
};

function swap(json) {
	var ret = {};
	for (var key in json) {
		ret[json[key]] = key;
	}
	return ret;
}

var colorMapingSwaped = swap(colorMaping);

// create functionality for pressing button animation
function showPressingButton(chosenColor) {
	$("." + chosenColor + "-button").click(function () {
		$("." + chosenColor + "-button").addClass(chosenColor + "-button-pressed");
		setTimeout(function () {
			$("." + chosenColor + "-button").removeClass(chosenColor + "-button-pressed");
		}, 150);
	});
}

for (var i = 0; i < colorArray.length; i++) {
	showPressingButton(colorArray[i]);
}

// functions for pressing start, reset buttons, the interface buttons ----------
function showPressingButtonInterface(chosenColor) {
	$("." + chosenColor + "-body-button").click(function () {
		$("." + chosenColor + "-body-button").addClass(chosenColor + "-button-pressed");
		setTimeout(function () {
			$("." + chosenColor + "-body-button").removeClass(chosenColor + "-button-pressed");
		}, 150);
	});
}

for (var i = 0; i < colorInterfaceButtons.length; i++) {
	showPressingButtonInterface(colorInterfaceButtons[i]);
}

// lighting the buttons in order
function lightButtons(chosenColor) {
	$("." + chosenColor + "-button").addClass(chosenColor + "-button-lighted");
	setTimeout(function () {
		$("." + chosenColor + "-button").removeClass(chosenColor + "-button-lighted");
	}, 700);
}

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}


// code for catching which buttons are being pressed --------------

var arrayCollectPressing = [];

function catchPressButton(chosenColor) {
	$("." + chosenColor + "-button").click(function () {
		arrayCollectPressing.push(colorMaping[chosenColor]);
		console.log(arrayCollectPressing);
	});
}

for (var i = 0; i < colorArray.length; i++) {
	catchPressButton(colorArray[i]);
}

function catchPressInteractButton(chosenColor) {
	$("." + chosenColor + "-body-button").click(function () {
		switch (chosenColor) {
			case "green":
				console.log("Button pressed: start.");
				break;
			case "red":
				console.log("Button pressed: strict.");
				break;
			case "yellow":
				console.log("Button pressed: reset.");
				break;
			default:
				break;
		}
	});
}

for (var i = 0; i < colorInterfaceButtons.length; i++) {
	catchPressInteractButton(colorInterfaceButtons[i]);
}





// for lighting the buttons in order --------------------
// var orderLights = [0, 1, 3, 2, 0];

async function lightButtonsInOrder(orderLights) {
	for (var i = 0; i < orderLights.length; i++) {
		var chosenColor = colorMapingSwaped[orderLights[i]];
		await sleep(700);
		lightButtons(chosenColor);
	}
}

// lightButtonsInOrder(orderLights);
