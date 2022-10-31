"use strict";
let lname = "Diffie";
// lname = 19;
// type inference
// does not need to define the datatype
let fname = "Mark";
let newname = lname.toUpperCase();
console.log(newname);
// declare
let age;
// assign
age = 25;
let dob = "25";
let result = parseInt(dob);
let isValid; // by default this is undefined
// console.log(isValid); // this gives an error
// every non assigned variable have the value of undefined
let isOk = false;
console.log(isOk);
// ------------------------------
// two ways of declaring arrays
let empList;
// the generics syntax
let depList;
// empList = ["a", "b", 10]; // this gives an error
let numList;
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
// Design System
let c = 1 /* Color.Green */;
// Tuples
let swapNumbs;
function swapNumbers(num1, num2) {
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
