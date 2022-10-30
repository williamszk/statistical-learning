// outputResult comes from the vendor file
// the vendor file should be loaded before
// or maybe we should import the vendor file inside this file

const defaultResult = 0;
let logEntries = [];
let currentResult = defaultResult;

/**
 * Gets input from input field
 * @returns
 */
function getUserNumberInput() {
	return parseInt(usrInput.value);
}

/** Generates and writes to the screen the calculation description*/
function createAndWriteOutput(operator, initialResult, calcNumber) {
	const description = `${initialResult} ${operator} ${calcNumber}`;
	outputResult(currentResult, description); // note: currentResult is a global state variable
}

function writeToLog(operation, prevResult, operand, result) {
	logEntry = {
		operation,
		prevResult,
		operand,
		result,
	};
	logEntries.push(logEntry);
}

function add() {
	const enteredNumber = getUserNumberInput();
	const initialResult = currentResult;
	currentResult += enteredNumber;
	createAndWriteOutput("+", initialResult, enteredNumber);
	writeToLog("ADD", initialResult, enteredNumber, currentResult);
	console.log(logEntries);
}

function subtract() {
	const enteredNumber = getUserNumberInput();
	const initialResult = currentResult;
	currentResult -= enteredNumber;
	createAndWriteOutput("-", initialResult, enteredNumber);
	writeToLog("SUBTRACT", initialResult, enteredNumber, currentResult);
	console.log(logEntries);
}

function multiply() {
	const enteredNumber = getUserNumberInput();
	const initialResult = currentResult;
	currentResult *= enteredNumber;
	createAndWriteOutput("*", initialResult, enteredNumber);
	writeToLog("MULTIPLY", initialResult, enteredNumber, currentResult);
	console.log(logEntries);
}

function divide() {
	const enteredNumber = getUserNumberInput();
	const initialResult = currentResult;
	currentResult /= enteredNumber;
	createAndWriteOutput("/", initialResult, enteredNumber);
	writeToLog("DIVIDE", initialResult, enteredNumber, currentResult);
	console.log(logEntries);
}

addBtn.addEventListener("click", add);
subtractBtn.addEventListener("click", subtract);
multiplyBtn.addEventListener("click", multiply);
divideBtn.addEventListener("click", divide);
