// 
// https://www.youtube.com/watch?v=jS4aFq5-91M

// console.log(document)
// console.log(typeof(document))

let count = 0
let elemCountEl = document.getElementById("count-el")
// console.log("elemCountEl:", elemCountEl)
elemCountEl.textContent = count

elemPreviusEntries = document.getElementById("saved-counts")
// console.log(elemPreviusEntries)
elemPreviusEntries.textContent += "Previous Entries: "


// console.log("elemCountEl tyepof:", typeof(elemCountEl))

// let elemCountShow = document.getElementById("count-show")
// console.log("elemCountShow:", elemCountShow)

let elemWelcome = document.getElementById("welcome-el")
// console.log(elemWelcome)

let namePassenger = "Bobson Bobstein"
let greeting = "Welcome to the station"
let emojiGreeting = " ✌️"
elemWelcome.textContent = greeting + ", " + namePassenger+emojiGreeting



function increment() {
    count += 1
    elemCountEl.textContent = count

}

function remove(){
    count -= 1
    if (count < 0){
        count = 0
    }
    elemCountEl.textContent = count
}

// function showCount(){
//     elemCountShow.textContent = count
// }


function save() {
    elemPreviusEntries.textContent += count +" - "
    count = 0
    elemCountEl.textContent = count
}

function reset(){
    count = 0
    elemCountEl.textContent = count
}


let firstName = "William"
let lastName = "Suzuki"
let fullName = firstName + " " + lastName
// console.log("fullName:",fullName)

function concatenateStrings(string1, string2, sep=" "){
    return string1+sep+string2
}

concatenetedStrings = concatenateStrings(firstName, lastName)
// console.log("From function concatenateStrings():",concatenetedStrings)


// let namePerson = "Linda"
// let greeting2 = "Hi there"
// console.log(concatenateStrings(greeting2,namePerson, sep=", "))

let myPoints = 3

function add3Points(){
    myPoints += 3
}

function remove1Points(){
    myPoints -= 1
}


add3Points()
add3Points()
add3Points()
remove1Points()
remove1Points()
// console.log(myPoints)

