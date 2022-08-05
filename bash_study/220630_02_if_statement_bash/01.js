
// test with && in java script

console.log("// ======================== 1 ======================== //"); 
false && console.log("General Kenobi")

console.log("// ======================== 2 ======================== //"); 
true && console.log("General Kenobi")

console.log("// ======================== 3 ======================== //"); 
// console.log(kkk) && console.log("General Kenobi");
// this will break the code
// in the case of javascript the && will work with true and false
// or truthy and falsy values

console.log("// ======================== 4 ======================== //"); 
true || console.log("General Kenobi")
false || console.log("General Skywalker")

// with || if the condition is true, it will not run the second,
// if the first condition is false, then it will run the second

console.log("// ======================== 5 ======================== //"); 
1 || console.log("General Kenobi")
undefined || console.log("General Skywalker")
0 || console.log("General Organa")
