// use jQuery to make the game work

// array of color used in other places
var colorArray = ["blue", "red", "yellow", "green"];
var quantityColors = colorArray.length;
var colorInterfaceButtons = ["green", "red", "yellow"];
var simonGameStarted = false;
var waitUserInput = false;
var orderedLights = [];
var orderedButtonsPressed = [];

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
  $("." + chosenColor + "-button").click(function() {
    $("." + chosenColor + "-button").addClass(chosenColor + "-button-pressed");
    setTimeout(function() {
      $("." + chosenColor + "-button").removeClass(chosenColor + "-button-pressed");
    }, 150);
  });
}

for (var i = 0; i < quantityColors; i++) {
  showPressingButton(colorArray[i]);
}

// functions for pressing start, reset buttons, the interface buttons ----------
function showPressingButtonInterface(chosenColor) {
  $("." + chosenColor + "-body-button").click(function() {
    $("." + chosenColor + "-body-button").addClass(chosenColor + "-button-pressed");
    setTimeout(function() {
      $("." + chosenColor + "-body-button").removeClass(chosenColor + "-button-pressed");
    }, 150);
  });
}

for (var i = 0; i < colorInterfaceButtons.length; i++) {
  showPressingButtonInterface(colorInterfaceButtons[i]);
}

// lighting the buttons in order
function lightButtonsSelectedColor(chosenColor) {
  $("." + chosenColor + "-button").addClass(chosenColor + "-button-lighted");
  setTimeout(function() {
    $("." + chosenColor + "-button").removeClass(chosenColor + "-button-lighted");
  }, 700);
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


// code for catching which buttons are being pressed --------------


function isUserInputEqualToTrueSequence(orderedButtonsPressed, orderedLights) {
  if (orderedButtonsPressed.length === orderedLights.length && orderedLights.length !== 0) {
    waitUserInput = false;
    for (var i = 0; i < orderedButtonsPressed.length; i++) {
      if (orderedButtonsPressed[i] !== orderedLights[i]) {
        return false;
      }
    }
    // the only alternative left if the loop never gets to false
    // is that all values are equal, so the answer is correct
    return true;
  } else {
    return false;
  }
}

function isGameOver(isUserInputCorrect) {
  if (isUserInputCorrect) {
    // the only situation here is when the user got right the color sequence
    return false;
  } else if (waitUserInput) { // isUserInputCorrect -> false
    // if isUserInputCorrect <- false, it can be that the player is still playing;
    return false;
  } else { // waitUserInput -> false; isUserInputCorrect -> false
    // the only option left is if the player made a mistake
    return true;
  }
}

function resetPointsCounter() {
  $(".text-counter-white-body").html("--");
}

function terminateGame(checkIsGameOver) {
  if (checkIsGameOver) {
    // reset all global variables to the start value
    simonGameStarted = false;
    waitUserInput = false;
    orderedLights = [];
    orderedButtonsPressed = [];
    resetPointsCounter();
    alert("Game Over!");
  }
}

function catchPressButton(chosenColor) {
  if (waitUserInput) {
    $("." + chosenColor + "-button").click(function() {
      orderedButtonsPressed.push(colorMaping[chosenColor]);
      console.log(orderedButtonsPressed);
      // check if the buttons pressed are the same as the true sequence
      var isUserInputCorrect = isUserInputEqualToTrueSequence(orderedButtonsPressed, orderedLights);
      // false and lengths are the same, and waiting for user input, then game over
      // true, increase one point
      // false, wait for user input
      var checkIsGameOver = isGameOver(isUserInputCorrect);
      terminateGame(checkIsGameOver);


    });
  } else {
    console.log("Color button pressed, but not program is not waiting for user input. Start the game first.")
  }
};

for (var i = 0; i < quantityColors; i++) {
  catchPressButton(colorArray[i]);
}

function startSimonGame() {
  if (!simonGameStarted) {
    simonGameStarted = true;
    waitUserInput = true;
    increasePointInHtml();
    var randomNumberColor = Math.floor(Math.random() * quantityColors)
    orderedLights.push(randomNumberColor);
    lightButtonsInOrder(orderedLights);
    console.log(orderedLights);
  } else {
    alert("Game already started.");
  }
}

function catchPressInteractButton(chosenColor) {
  $("." + chosenColor + "-body-button").click(function() {
    switch (chosenColor) {
      case "green":
        console.log("Button pressed: start.");
        startSimonGame();
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

// function increase the quantity in the counter
// of the white body
function increasePointsCounter() {
  var valueCounter = $(".text-counter-white-body").html();
  if (valueCounter === "--") {
    valueCounter = 0;
  } else {
    valueCounter = parseInt(valueCounter);
    valueCounter++;
  }
  return valueCounter;
}

function includeZeroToPointCounter(valueCounter) {
  if (parseInt(valueCounter) < 10) {
    return "0" + valueCounter.toString();
  } else {
    return valueCounter.toString();
  }
}

function increasePointInHtml() {
  var increasedPoint = increasePointsCounter();
  var pointStringIncreased = includeZeroToPointCounter(increasedPoint);
  $(".text-counter-white-body").html(pointStringIncreased);
}

// below is just an example of how to use the function
// increasePointInHtml();


// for lighting the buttons in order --------------------
// var orderLights = [0, 1, 3, 2, 0];

async function lightButtonsInOrder(orderLights) {
  for (var i = 0; i < orderLights.length; i++) {
    var chosenColor = colorMapingSwaped[orderLights[i]];
    await sleep(700);
    lightButtonsSelectedColor(chosenColor);
  }
}

// lightButtonsInOrder(orderLights);