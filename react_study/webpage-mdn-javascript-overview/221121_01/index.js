// Arrays in JavaScript are actually a special type of object

// Array literal
const a = ["dog", "cat", "hen"];
a.length; // 3

const a1 = ["dog", "cat", "hen"];
a1[100] = "fox"; // include item far in the index number
console.log(a1.length); // 101
console.log(a1); // ['dog', 'cat', 'hen', empty × 97, 'fox']

console.log(typeof a1); // object

const a2 = ["dog", "cat", "hen"];
console.log(typeof a2[90]); // undefined

for (const currentValue of a) {
	// Do something with currentValue
	console.log(currentValue);
}
const animals = ["dog", "cat", "hen"];
const babies = animals.map((name) => `baby ${name}`);
// babies = ['baby dog', 'baby cat', 'baby hen']
console.log(babies);
