let var1 = 1;
let var2 = var1;

console.log("var1: ", var1);
console.log("var2: ", var2);

// change var1, let's see if var2 is also changed
var1 = 3;
console.log("After change:");
console.log("var1: ", var1);
console.log("var2: ", var2);

// var1:  1
// var2:  1
// After change:
// var1:  3
// var2:  1

// Experiment with an Object
let obj1 = { a: 10 };
let obj2 = obj1;

console.log("obj1: ", obj1);
console.log("obj2: ", obj2);

// Change the the value inside obj1 and see if it changed in obj2
obj1.a = 99;
console.log("After the change: ");
console.log("obj1: ", obj1);
console.log("obj2: ", obj2);
// obj1:  { a: 10 }
// obj2:  { a: 10 }
// After the change:
// obj1:  { a: 99 }
// obj2:  { a: 99 }

// Note that both objects changed
// in the case of composite objects like Objects and Arrays
// the variable behaves like a binding
// it is more like a tentacle than a box
// a binding will reference a box that contain some value
