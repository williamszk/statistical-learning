const fs = require("fs");
const superheroes = require("superheroes");
const supervillains = require("supervillains");


// fs.copyFileSync("./file1.txt", "file1-copy.txt");
let mySuperHero = superheroes.random();
let mySuperVillain = supervillains.random();

console.log("mySuperHero:", mySuperHero);
console.log("mySuperVillain:", mySuperVillain);

// to initialize a new package in node
// npm init

// this will create a file package.json
// which will keep track of the packages that we use in this particular project
// npm install superheroes
// npm install supervillains