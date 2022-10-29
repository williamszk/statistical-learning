// functions

function add(a: number, b: number): number {
	return a + b;
}

function myFunc(): void {
	10 + 10;
}

// this is an arrow function
const subtract = (a: number, b: number): number => a - b;

// this is a function expression
const mult = function (a: number, b: number): number {
	return a * b;
};

// generic function

// optional parameters
function add2(num1: number, num2: number, num3?: number): number {
	const result: number = num3 ? num1 + num2 + num3 : num1 + num2;
	return result;
}

// default argument
// required parameters
function add3(num1: number, num2: number, num3: number = 3): number {
	const result = num1 + num2 + num3;
	return result;
}

// rest parameters
// we use the spread operator ... 
function add4(num1: number, num2: number, ...num3: number[]): number {
	return num1 + num2 + num3.reduce((a, b) => a + b, 0);
}

console.log(add4(1, 1, 1, 1, 1, 1, 1, 1));
