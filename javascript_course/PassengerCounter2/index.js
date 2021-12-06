// https://www.youtube.com/watch?v=jS4aFq5-91M&ab_channel=freeCodeCamp.org

// Subway passanger counter

// document.getElementById("count-el").innerText = 9

let count = 10

console.log("count =", count)


let myAge = 28

console.log("myAge =", myAge)

let humanDogRatio = 7

let myDogAge = myAge * humanDogRatio

console.log("myDogAge =",myDogAge)


let bonusPoints = 50
bonusPoints += 100
bonusPoints -= 25
bonusPoints += 70

console.log("bonusPoints =", bonusPoints)


function increment() {
  console.log("The botton was clicked.");
}


function countdown() {
  for (i=5; i >= 0; i--) {
    console.log(i)
  }
}

countdown()


let count1 = 20
let count2 = 10

function myFuncLogger() {
  let totalCount = count1 + count2
  console.log(totalCount)
}

myFuncLogger()

console.log(totalCount)

// in javascript we can't use a variable that is declared inside of a function
// console.log(totalCount)
// but inside the function we can access variables declared outside of it

// I remember that in SAS the "functions" which are macros can use and will produce
// variable outside of its scope, they are all global variables
// I am thinking about is this what we call a procedure?
























