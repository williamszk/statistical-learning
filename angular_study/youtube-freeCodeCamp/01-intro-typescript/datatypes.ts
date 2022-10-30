let lname = "Diffie";

// lname = 19;

// type inference
// does not need to define the datatype

let fname: string = "Mark";

let newname = lname.toUpperCase();

console.log(newname);

// declare
let age: number;

// assign
age = 25;

let dob = "25";
let result = parseInt(dob);

let isValid: boolean; // by default this is undefined
// console.log(isValid); // this gives an error
// every non assigned variable have the value of undefined

let isOk: boolean = false;
console.log(isOk);

// ------------------------------

// two ways of declaring arrays
let empList: string[];

// the generics syntax
let depList: Array<string>;

// empList = ["a", "b", 10]; // this gives an error

let numList: Array<number>;
numList = [1, 2, 3, 4];

let results = numList.filter((num) => {
	num > 2;
});

numList.filter((num) => {
	num < 10;
});

let result1 = numList.find((num) => {
	num === 2;
});
// let result1: number | undefined

let sumNum = numList.reduce((acc, num) => acc + num);

// stopped at:
// https://youtu.be/3qBXWUpoPHo?t=3638

const enum Color {
	Red,
	Green,
	Blue,
}
// Design System

let c: Color = Color.Green;

// Tuples
let swapNumbs: [number, number];

function swapNumbers(num1: number, num2: number): [number, number] {
	return [num2, num1];
}

swapNumbs = swapNumbers(10, 20);
console.log(swapNumbs);

swapNumbs[0];
swapNumbs[1];
// swapNumbs[2]; // this will give an error, given that it is a tuple

// any datatype
let department;
department = "IT";
department = 10;


// void


// never