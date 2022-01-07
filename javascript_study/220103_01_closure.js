// https://blog.logrocket.com/a-closer-look-at-javascript-closures-higher-order-functions-and-currying/#:~:text=Closures%20are%20integral%20to%20higher,a%20*%20b%3B%20%7D%20console.

// node

// Imagine a situation where we have a function (myFunc) that needs to access a variable that is
// in the outer scope (outerVar). 
// outerVar could be in the global scope, this is a way that this can happen.
// But we don't like global variables, we like local variables.
// We can make outerVar be a local var using a higher order function
// 

// ---------------------------------------------- //
// situation where outerVar is a global variable

var outerVar = 10;

const myFunc = () => {
    console.log("Ran with the outerVar: " + outerVar);
}

myFunc()

// ---------------------------------------------- //
// situation where outerVar is a local variable

const higherFunc = () => {
    var outerVar = 99;
    const myFunc = () => {
        console.log("Ran with the outerVar: " + outerVar);
    }

    myFunc();
}
// to be able to use outerVar, I needed to redefine the function
// inside the higher order function
// I think this is what we call a closure

higherFunc()

// ---------------------------------------------- //
const myFunc = () => {
    console.log("Ran with the outerVar: " + outerVar);
}

const higherFunc = (myFunc) => {
    var outerVar = 99;
    myFunc();
}

higherFunc(myFunc);
// this doesn't work
// to be able to use an outer variable inside the function
// in the moment that we define the function the outer variable
// must be in existance

// ---------------------------------------------- //


// ---------------------------------------------- //