"use strict";
// functions
function add(a, b) {
    return a + b;
}
function myFunc() {
    10 + 10;
}
// this is an arrow function
const subtract = (a, b) => a - b;
// this is a function expression
const mult = function (a, b) {
    return a * b;
};
// generic function
// optional parameters
function add2(num1, num2, num3) {
    const result = num3 ? num1 + num2 + num3 : num1 + num2;
    return result;
}
// default argument
// required parameters
function add3(num1, num2, num3 = 3) {
    const result = num1 + num2 + num3;
    return result;
}
// rest parameters
// we use the spread operator ...
function add4(num1, num2, ...num3) {
    return num1 + num2 + num3.reduce((a, b) => a + b, 0);
}
console.log(add4(1, 1, 1, 1, 1, 1, 1, 1));
// generics
function getItems(items) {
    return new Array().concat(items);
}
let result01 = getItems([1, 2, 3, 4]);
console.log(result01);
let result02 = getItems(["a", "b", "c"]);
console.log(result02);
// we can explicitly pass the type into the function invocation
let result03 = getItems([1, 2, 3, 4]);
console.log(result03);
let result04 = getItems(["a", "b", "c"]);
console.log(result04);
