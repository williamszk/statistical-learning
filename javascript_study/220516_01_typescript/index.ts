import * as _ from "lodash";

// https://www.youtube.com/watch?v=ahCwqrYpIuM&ab_channel=Fireship

// typescript does not run in the browser nor in node, we need the typescript compiler
// to transform the typescript code into javascript

console.log("hello world");

// by default typescript will compile to ES3

async function hello() {
  return "hello";
}

// we create a tsconfig.json
// this file will contain the configuration for the tsc
// so that we can change e.g. the ES version

// const url = new URL()

let lucky = 23;
// lucky = "23"; // this gives an error

// this is a way to assign any type to this variable
let lucky2: any = 23;

type Style = string;

let font: Style;

// this is like a C union, the variable of this type, can only assume values
// of bold, intalic or 23
type Sylized = "bold" | "italic" | 23;

let myFont: Sylized;

// myFont = "something"; // this will give an error
myFont = 23;
myFont = "italic";

// enforce the shape of an object
// for this we use the interface
// in programming and OOP, the internface of the set of methods and fields of a class
// but in typescript, interface is the signature of an object, or its shape

interface Person {
  first: string;
  last: string;
  [key: string]: any;
}
// the typescript interface reminds of a typedef struct from C
// or type struct from Go

const person01: Person = {
  first: "Jeff",
  last: "Delaney",
};

const person02: Person = {
  first: "Usain",
  last: "Bolt",
  fast: true,
};

// functions in typescript

function pow(x: number, y: number): string {
  return Math.pow(x, y).toString();
}
// we could also use void

const arr: number[] = [];

arr.push(1);
// arr.push("23");
// arr.push(false);

// this is an arrey of people
const arr02: Person[] = [];

// there is tuple in typescript
type MyList = [number?, string?, boolean?];
const myTuple01: MyList = [];

// typescript generics
class Observable<T>{
    constructor(public value: T){

    }
}

let x: Observable<number>;

let y: Observable<Person>;

let z = new Observable(23);

