// https://youtu.be/jS4aFq5-91M?t=5187

let num1 = 8;
let num2 = 2;
let result = "Result";

document.getElementById("num1-el").textContent = num1;
document.getElementById("num2-el").textContent = num2;
document.getElementById("sum-el").textContent = result;

function add() {
  document.getElementById("sum-el").textContent = num1 + num2;
}

function subtract() {
  document.getElementById("sum-el").textContent = num1 - num2;
}

function divide() {
  document.getElementById("sum-el").textContent = num1 / num2;
}

function multiply() {
  document.getElementById("sum-el").textContent = num1 * num2;
}

// render the result in "sum-el"
