const myDate02 = new Date(1995, 11, 17);
console.log(typeof myDate02); // object

console.log(myDate02.__proto__); // object

const personPrototype = {
	greet() {
		console.log("hello!");
	},
};

const carl = Object.create(personPrototype);
carl.greet(); // hello!

console.log(typeof carl);
console.log(carl.__proto__);

// Stopped here:
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes#setting_a_prototype

