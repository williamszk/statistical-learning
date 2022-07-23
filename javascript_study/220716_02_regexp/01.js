
 // https://javascript.info/regexp-introduction

// we can create regex using a class to instantiate or
// or we can use the /.../ syntax
let myRegEx = new RegExp("a*", "g");

console.log(typeof myRegEx); // object

myRegEx2 = /a*/; // no pattern

console.log(typeof myRegEx2); // object


myRegEx2 = /a*/g; 
// Slashes /.../ tell JavaScript that we are creating a regular expression. They play the same role as quotes for strings


// about flags in patterns
// i: case insensitive
// g: look for all matches
// 




