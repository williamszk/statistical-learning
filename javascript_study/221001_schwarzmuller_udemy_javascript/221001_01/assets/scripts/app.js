// alert("This workd!");

const defaultResult = 0;

let currentResult = defaultResult;


currentResult = ((currentResult + 10) * 3) / 2 - 1;

// let calculationDescription = "(" + defaultResult + " + 10) * 3 / 2 - 1";
// an alternative way to interpolate strings
// this is called template literal:
let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`;


outputResult(currentResult, calculationDescription);
