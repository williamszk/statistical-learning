document.writeln('Hello, World!')

document.writeln(2e10) // 20000000000
document.writeln(2e5) // 200000

NaN
document.writeln(typeof(NaN)) // number
document.writeln(isNaN(NaN)) // true
document.writeln(NaN == NaN) // false

document.writeln(typeof [1,2,3]) // object, this is wrong
document.writeln(typeof null) // object, this is wrong


document.writeln(typeof undefined) // undefined

var stooge = {
    "first-name": "Jerome",
    "last-name": "Howard"
};


var flight = {
    airline: "Oceanic",
    number: 815,
    departure: {
        IATA: "SYD",
        time: "2004-09-22 14:55",
        city: "Sydney"
    },
    arrival: {
        IATA: "LAX",
        time: "2004-09-23 10:42",
        city: "Los Angeles"
    }
};

var middle = stooge["middle-name"] || "(none)";
// stooge["middle-name"] doesn't exist so it will return undefined
// undefined is a falsy value, then || will make the string "(none)"
// be returned

document.writeln(middle) // (none) 

var status = flight.status || "unknown";
// we can use || to include a default value in case the key
// is not present
document.writeln(status) // unknown 

// Optional chaining (?.)
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining


var statusPostion = (flight.status || null).position


