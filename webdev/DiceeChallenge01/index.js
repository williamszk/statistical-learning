const numSideDice = 6;

function createDicePoint(diceElement, position = "position-center") {
  diceElement.appendChild(document.createElement("div"));
  diceElement.lastChild.classList.add("dice-point");
  diceElement.lastChild.classList.add(position);
}

function removeCenterDicePoint(diceElement) {
  diceElement.removeChild(diceElement.querySelector(".dice-point.position-center"));
}

function setDiceToOne(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-center");

}

function setDiceToTwo(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-bottom-left");
  createDicePoint(diceElement, position = "position-upper-right");
}

function setDiceToThree(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-bottom-left");
  createDicePoint(diceElement, position = "position-upper-right");
  createDicePoint(diceElement, position = "position-center");
}

function setDiceToFour(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-bottom-left");
  createDicePoint(diceElement, position = "position-upper-right");
  createDicePoint(diceElement, position = "position-upper-left");
  createDicePoint(diceElement, position = "position-bottom-right");
}

function setDiceToFive(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-bottom-left");
  createDicePoint(diceElement, position = "position-upper-right");
  createDicePoint(diceElement, position = "position-upper-left");
  createDicePoint(diceElement, position = "position-bottom-right");
  createDicePoint(diceElement, position = "position-center");
}

function setDiceToSix(idDicePlayer = "dice-player-1") {
  var diceElement = document.getElementById(idDicePlayer);
  removeCenterDicePoint(diceElement);
  createDicePoint(diceElement, position = "position-bottom-left");
  createDicePoint(diceElement, position = "position-upper-right");
  createDicePoint(diceElement, position = "position-upper-left");
  createDicePoint(diceElement, position = "position-bottom-right");
  createDicePoint(diceElement, position = "position-center-right");
  createDicePoint(diceElement, position = "position-center-left");
}

function setDiceValue(result, idDicePlayer = "dice-player-1") {
  switch (result) {
    case 1:
      setDiceToOne(idDicePlayer);
      break;
    case 2:
      setDiceToTwo(idDicePlayer);
      break;
    case 3:
      setDiceToThree(idDicePlayer);
      break;
    case 4:
      setDiceToFour(idDicePlayer);
      break;
    case 5:
      setDiceToFive(idDicePlayer);
      break;
    case 6:
      setDiceToSix(idDicePlayer);
      break;
  }
}

// setDiceToSix(idDicePlayer = "dice-player-1")
// setDiceToSix(idDicePlayer = "dice-player-2")
// setDiceToFive(idDicePlayer = "dice-player-2")
// setDiceToFour(idDicePlayer = "dice-player-2")
// setDiceToThree(idDicePlayer = "dice-player-2")
// setDiceToTwo(idDicePlayer = "dice-player-2")

var resultPlayer1 = Math.ceil(Math.random() * numSideDice);
var resultPlayer2 = Math.ceil(Math.random() * numSideDice);

console.log("resultPlayer1 = ", resultPlayer1);
console.log("resultPlayer2 = ", resultPlayer2);
setDiceValue(resultPlayer1, idDicePlayer = "dice-player-1");
setDiceValue(resultPlayer2, idDicePlayer = "dice-player-2");

if (resultPlayer1 > resultPlayer2) {
  document.getElementById("title-result").innerHTML = '<span class="flag-result"><i class="fas fa-flag"></i></span> Player 1 Wins!'
} else if (resultPlayer2 > resultPlayer1) {
  document.getElementById("title-result").innerHTML = '<span class="flag-result"><i class="fas fa-flag"></i></span> Player 2 Wins!'
} else {
  document.getElementById("title-result").innerHTML = 'It was a tie!'
}