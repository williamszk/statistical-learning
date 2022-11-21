Number;
BigInt;
String;
Boolean;
Symbol;
undefined;
null;

console.log(3 / 2); // 1.5, not 1
console.log(0.1 + 0.2); // 0.30000000000000004

console.log(0b111110111); // 503
console.log(0o767); // 503
console.log(0x1f7); // 503
console.log(5.03e2); // 503

console.log(typeof 0b0100);

//  BigInt we need to use the n suffix
console.log(-3n / 2n); // -1n
console.log(typeof 10n);

Math.sin(3.5);
r = 10;
const circumference = 2 * Math.PI * r;

console.log(parseInt("1000"));
console.log(parseInt("1000sdkajskdasdasd")); // 1000
console.log(parseInt("sdfsdfsd1000")); // NaN
console.log(parseFloat("10.2982dkfas")); // 10.2982
console.log(parseFloat("1.2d12222")); // 1.2

console.log(Number("10.2932")); // 10.2932
console.log(+"10.2932"); // 10.2932

console.log(Number("10.2932ddd")); // NaN
console.log(+"10.2932ddd"); // NaN
// + is a shorthand for Number

// NaN and Infinity are number type
console.log(typeof NaN); // number
console.log(typeof Infinity); // number

console.log(Math.log(-1)); // NaN
console.log(1 / 0); // Infinity

console.log(NaN * 10); // NaN
console.log(NaN === NaN); // false
// NaN is the only number that is not equal to itself
console.log(10 === 10); // true
console.log(Infinity === Infinity); // true

// JS use utf-16
console.log("Hello, world");
console.log("你好，世界！"); // Nearly all Unicode characters can be written literally in string literals

// all primitive datatypes are immutable
// when we operate on them we create a new instance of the primitive data type

console.log("Hello There".length);

const age = 25;
console.log("I am " + age + " years old."); // String concatenation
console.log(`I am ${age} years old.`); // Template literal
// here we use back ticks
// this is called template literal
// In python we would use f-string and in C# string interpolation

// the difference between null and undefined
// null is a human made value
// undefined is not

// null pass the info that the value should be null
// undefined does not pass this info

let a;
let name = "Simon";

// myLetVariable is *not* visible out here

for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
	// myLetVariable is only visible in here
}

// myLetVariable is *not* visible out here

// this is a block of code
{
	let myLetVariable = 10;
	console.log("myLetVariable: " + myLetVariable);
}

const Pi = 3.14; // Declare variable Pi
console.log(Pi); // 3.14

// const Pi = 3.14;
Pi = 1; // will throw an error because you cannot change a constant variable.

const obj = {};
obj.a = 1; // no error
console.log(obj); // { a: 1 }

// take a look at this later
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let

function foo(x, condition) {
	if (condition) {
		console.log(x);
		const x = 2;
		console.log(x);
	}
}

foo(1, true); // this surprisingly throws an error

// simple == makes type coercion
5 == "5"; // true
5 === "5"; // false

1 == true; // true
1 === true; // false

// short-circuit logic
// return the value that already determines the result
0 && "Hello"; // 0
"hello" && 0 && "world"; // 0
"hello" && "world" && "foo"; // "foo"
0 || "Hello"; // "Hello"
0 || "" || "bar"; // bar

const o = null;
const name1 = o && o.getName();

// if cachedName is falsy, null e.g.
// then cachedName is assigned the value from getName()
// the name2 variable is assigned cachedName value
const name2 = cachedName || (cachedName = getName());

let a1 = (b1 = 10);
// a1 is 10

let name02 = "kittens";
if (name02 === "puppies") {
	name02 += " woof";
} else if (name02 === "kittens") {
	name02 += " meow";
} else {
	name02 += "!";
}
name02 === "kittens meow";

while (true) {
	// an infinite loop!
}

let input;
do {
	input = get_input();
} while (inputIsNotValid(input));

for (let i = 0; i < 5; i++) {
	// Will execute 5 times
}

const array01 = [1, 2, 3];
for (const value of array01) {
	// do something with value
	console.log(value);
}

const object02 = {
	a: 1,
	b: 2,
	c: 2,
};
for (const property in object02) {
	// do something with object02 property
	console.log(property);
	// prints the key
}

switch (action) {
	case "draw":
		drawIt();
		break;
	case "eat":
		eatIt();
		break;
	default:
		doNothing();
}

function foo() {}

try {
	buildMySite("./website");
} catch (e) {
	console.error("Building site failed:", e);
}

function buildMySite(siteDirectory) {
	if (!pathExists(siteDirectory)) {
		throw new Error("Site directory does not exist");
	}
}

Error;
typeof Error;

throw new Error("Error message");

TypeError;
RangeError;

{
	let a = 10;
	a instanceof Number;
}

const obj = {
	name: "Carrot",
	for: "Max",
	details: {
		color: "orange",
		size: 12,
	},
};

obj.name;
obj.age || null;
0 || "" || false;

obj["name"];

// if age is not set then return a default value
const defaultAge = 10;
obj["age"] || defaultAge;

{
	// Dot notation
	obj.name = "Simon";
	const name = obj.name;
}

{
	// Bracket notation
	obj["name"] = "Simon";
	const name = obj["name"];
}

{
	// Can use a variable to define a key
	const userName = prompt("what is your key?");
	obj[userName] = prompt("what is its value?");
}

a = Symbol(10);
typeof a;

obj.details.color; // orange
obj["details"]["size"]; // 12

// objects are references
const me = {};
const stillMe = me;
me.x = 1;
console.log(stillMe.x); // 1

// What are prototypes in javascript?
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

const myObject = {
	city: "Madrid",
	greet() {
		console.log(`Greetings from ${this.city}`);
	},
};

myObject.greet(); // Greetings from Madrid

Object.keys(myObject);
myObject.toString(); // [object Object]
Object.getPrototypeOf(myObject); //  Object {}

// below both are the same 
myObject.__proto__
Object.getPrototypeOf(myObject)

typeof myObject.__proto__ // object

myObject.__proto__.__proto__ // null

typeof null // object
// this is strange, shouldn't it be like null type, or something like it

// both of those will give an error
null.__proto__
myObject.__proto__.__proto__.__proto__

// =============================== //
const myDate = new Date();
let object = myDate;
typeof myDate
object === myDate

do {
  object = Object.getPrototypeOf(object);
  console.log(object);
} while (object);

// Date.prototype
// Object { }
// null

// {}
// [Object: null prototype] {}
// null
// undefined
myDate.__proto__ // {}
Object.getPrototypeOf(myDate) // {}

myDate.__proto__.__proto__ // 

// =========================
const myDate02 = new Date(1995, 11, 17);
typeof myDate02 // object
Object.keys(myDate02) // []
Object.keys(myDate02.__proto__) // []
Object.keys(myDate02.__proto__.__proto__) // []
Object.keys(myDate02.__proto__.__proto__.__proto__) // this gives error
console.log(myDate02.getYear()); // 95

myDate02.getYear = function () {
  console.log("something else!");
};

myDate02.getYear(); // 'something else!'