// use jQuery to make the game work

// array of color used in other places
const colorArray = ["blue", "red", "yellow", "green"];
const quantityColors = colorArray.length;
const colorInterfaceButtons = ["green", "red", "yellow"];


// var simonGameStarted = false;
// var waitUserInput = false;
// var orderedLights = [];
// var orderedButtonsPressed = [];


const colorMaping = {
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

const colorMapingSwaped = swap(colorMaping);



// create functionality for pressing button animation
function showPressingButton(chosenColor) {
  $("." + chosenColor + "-button").click(function() {
    $("." + chosenColor + "-button").addClass(chosenColor + "-button-pressed");
    setTimeout(function() {
      $("." + chosenColor + "-button").removeClass(chosenColor + "-button-pressed");
    }, 150);
  });
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


// lighting the buttons in order
function lightButtonsSelectedColor(chosenColor) {
  // this does not change state, only affect UI
  $("." + chosenColor + "-button").addClass(chosenColor + "-button-lighted");
  setTimeout(function() {
    $("." + chosenColor + "-button").removeClass(chosenColor + "-button-lighted");
  }, 700);
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


// code for catching which buttons are being pressed --------------

function isUserInputEqualToTrueSequence(stateControl) {
  if (stateControl.orderedButtonsPressed.length === stateControl.orderedLights.length && stateControl.orderedLights.length !== 0) {
    // this is the case when the user finished to play his colors
    // so we don't need to wait for user input
    // why do we need this state control variable?
    stateControl.waitUserInput = false;
    for (var i = 0; i < stateControl.orderedButtonsPressed.length; i++) {
      if (stateControl.orderedButtonsPressed[i] !== stateControl.orderedLights[i]) {
        stateControl.isInputCorrect = false;
        return stateControl;
      }
    }
    // the only alternative left if the loop never gets to false
    // is that all values are equal, so the answer is correct
    stateControl.isInputCorrect = true;
    return stateControl;
  } else {
    // this is the case where the user didn't finished to input all his plays
    stateControl.isInputCorrect = false;
    stateControl.waitUserInput = true;
    return stateControl;
  }
}


function isGameOver(stateControl) {
  if (stateControl.isInputCorrect) {
    // the only situation here is when the user got right the color sequence
    stateControl.isGameOver = false;
    return stateControl;
  } else if (stateControl.waitUserInput) { // isUserInputCorrect -> false
    // if isUserInputCorrect == false, it can be that the player is still playing;
    stateControl.isGameOver = false;
    return stateControl;
  } else { // waitUserInput -> false; isUserInputCorrect -> false
    // the only option left is if the player made a mistake
    stateControl.isGameOver = true;
    return stateControl;
  }
}

function resetPointsCounter(stateControl) {
  // only interaction with UI
  $(".text-counter-white-body").html(stateControl.pointsCounter);
}


function terminateGame(stateControl) {
  if (stateControl.isGameOver) {
    alert("Game Over!");
    // stateControl = main();
    // console.log(stateControl);
    // resetPointsCounter(stateControl);
  }

  return stateControl;
}


function continueNextStep(stateControl) {
  if (!stateControl.isGameOver && !stateControl.waitUserInput && stateControl.simonGameStarted) {
    // this situation happens when the user finished to input his colors
    // and the game needs to update state control variables
    stateControl = increasePointInHtml(stateControl);

    keepRolling = true;
    while (keepRolling) {
      // this exists to not allow the game to have the same color followed twice.
      var randomNumberColor = Math.floor(Math.random() * quantityColors);
      if (randomNumberColor != stateControl.orderedLights[stateControl.orderedLights.length - 1]) {
        keepRolling = false;
      }
    }

    stateControl.orderedLights.push(randomNumberColor);

    lightButtonsInOrder(stateControl);
    stateControl.waitUserInput = true;
    stateControl.orderedButtonsPressed = []
  }
  return stateControl;
}


function catchPressButton(chosenColor, stateControl) {
  $("." + chosenColor + "-button").click(function() {
    if (stateControl.waitUserInput) {
      stateControl.orderedButtonsPressed.push(colorMaping[chosenColor]);
      console.log(stateControl.orderedButtonsPressed);
      // check if the buttons pressed are the same as the true sequence
      // var isUserInputCorrect = isUserInputEqualToTrueSequence(orderedButtonsPressed, orderedLights);
      stateControl = isUserInputEqualToTrueSequence(stateControl);
      // false and lengths are the same, and waiting for user input, then game over
      // true, increase one point
      // false, wait for user input
      // var checkIsGameOver = isGameOver(isUserInputCorrect);
      stateControl = isGameOver(stateControl);

      // in case the game is over:
      stateControl = terminateGame(stateControl);

      // true, increase one point and wait and then run the color sequence
      stateControl = continueNextStep(stateControl);

      return stateControl;

    } else {
      console.log(chosenColor + " color button pressed, but the program is not waiting for user input. Start the game first.")
      return stateControl;
    }
  });
  return stateControl;
};


function startSimonGame(stateControl) {
  if (!stateControl.simonGameStarted) {
    stateControl.simonGameStarted = true;
    stateControl.waitUserInput = true;
    stateControl = increasePointInHtml(stateControl);

    var randomNumberColor = Math.floor(Math.random() * quantityColors)
    stateControl.orderedLights.push(randomNumberColor);
    lightButtonsInOrder(stateControl);

    return stateControl;
  } else {
    alert("Game already started.");
    return stateControl;
  }
}


function catchPressInteractButton(chosenColor, stateControl) {
  $("." + chosenColor + "-body-button").click(function() {
    switch (chosenColor) {
      case "green":
        console.log("Button pressed: start.");
        console.log("stateControl before start Simon game:", stateControl); // delete me!
        stateControl = startSimonGame(stateControl);
        return stateControl;
      case "red":
        console.log("Button pressed: strict.");
        // need to implement the "strict" button
        return stateControl;
      case "yellow":
        console.log("Button pressed: reset.");
        // need to implement the "reset" button
        return stateControl;
      default:
        return stateControl;
    }
  });
  return stateControl;
}


// function increase the quantity in the counter
// of the white body

function includeZeroToPointCounter(valueCounter) {
  if (parseInt(valueCounter) < 10) {
    return "0" + valueCounter.toString();
  } else {
    return valueCounter.toString();
  }
}

function increasePointsCounter(stateControl) {

  if (stateControl.pointsCounter === $(".text-counter-white-body").html()) {
    // all correct
  } else {
    throw new Error('Error here!')
  }

  var valueCounter = stateControl.pointsCounter;
  if (valueCounter === "--") {
    valueCounter = 0;
  } else {
    valueCounter = parseInt(valueCounter);
    valueCounter++;
  }

  stateControl.pointsCounter = includeZeroToPointCounter(valueCounter);

  return stateControl;
}


function increasePointInHtml(stateControl) {
  stateControl = increasePointsCounter(stateControl);
  $(".text-counter-white-body").html(stateControl.pointsCounter);
  return stateControl
}

// below is just an example of how to use the function
// increasePointInHtml();


// for lighting the buttons in order --------------------
// var orderLights = [0, 1, 3, 2, 0];

async function lightButtonsInOrder(stateControl) {
  for (var i = 0; i < stateControl.orderedLights.length; i++) {
    var chosenColor = colorMapingSwaped[stateControl.orderedLights[i]];
    await sleep(700);
    lightButtonsSelectedColor(chosenColor);
  }
}




/*
As good practice create all functions outside of the main function.
In this way we can control which are the global variables.
Global values should be constants.
All variables that are shared between function in this way will need to be
explicitly refered as arguments to function or return from function.
The only variables that are accepted into function without being as arguments
are those that existed before the moment where we defined the function.
The only function that is allowed to be executed at the global scope is the 
main() function.

Maybe I'll not be able to build the design above
Because I'll need global variables to keep track of state
This is hard...

There are two situations where we need to interact with the outside world:
1. Interaction with the disk: e.g. databases, files, etc.
2. Interaction with the user interface.

The rest are internal operations, and those should be made of pure functions.

*/

function main() {

  var stateControl = {
    simonGameStarted: false,
    waitUserInput: false,
    orderedLights: [],
    orderedButtonsPressed: [],
    pointsCounter: "--",
    isInputCorrect: false,
    isGameOver: false
  }

  for (var i = 0; i < colorInterfaceButtons.length; i++) {
    // console.log("stateControl ", stateControl) // delete me!
    stateControl = catchPressInteractButton(colorInterfaceButtons[i], stateControl);
  }

  for (var i = 0; i < quantityColors; i++) {
    stateControl = catchPressButton(colorArray[i], stateControl);
  }

  for (var i = 0; i < colorInterfaceButtons.length; i++) {
    // just stateless interaction, no need for stateControl
    showPressingButtonInterface(colorInterfaceButtons[i]);
  }

  for (var i = 0; i < quantityColors; i++) {
    // just stateless interaction, no need for stateControl
    showPressingButton(colorArray[i]);
  }

  return stateControl;
}

stateControl = main();