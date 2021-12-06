// Chosen programming language:  JavaScript
// Chosen challenge platform:  reddit_dailyprogrammer
// Chosen challenge id:  110

// This is one of the programming challanges 

// easy challenge:
// https://www.reddit.com/r/dailyprogrammer/comments/12k3xr/1132012_challenge_110_easy_keyboard_shift/

// intermediate challenge
// https://www.reddit.com/r/dailyprogrammer/comments/12k3xt/1132012_challenge_110_intermediate_creepy_crawlies/


// difficult challenge
// https://www.reddit.com/r/dailyprogrammer/comments/12k3xw/1132012_challenge_110_difficult_you_cant_handle/



// --------------------------------------------------------------------------------------------- //
// let's try to table the easy challenge first
// https://www.goodtyping.com/teclatUSok.png

// You and a friend are working on a very important, bleeding-edge, research paper: "Computational Complexity 
// of Sorting Pictures of Cats with Funny Text on the Web". The catch though is your 
// friend wrote his part of the paper with his hands shifted to the right, meaning the top row of keys 
// he used weren't "QWERTYUIOP" (regular US keyboard), but instead "WERTYUIOP{".

// String ShiftedText - The shifted text in question. The only chracters you have to deal with 
// are letters, in both cases, and the following symbols: '{', '[', ':', ';', '<', ','. 
// The space character may be present, but you do not have to shift that.

// "Jr;;p ept;f" means "Hello World"
// "Lmiyj od ,u jrtp" means "Knuth is my hero"


mapDictionaryConverstion = {
    "{": "P",
    "[": "p",
    ":": "L",
    ";": "l",
    "p": "o",
    "l": "k",
    "<": "M",
    ",": "m",
    "o": "i",
    "k": "j",
    "m": "n",
    "i": "u",
    "j": "h",
    "n": "b",
    "u": "y",
    "h": "g",
    "b": "v",
    "y": "t",
    "g": "f",
    "v": "c",
    "t": "r",
    "f": "d",
    "c": "x",
    "r": "e",
    "d": "s",
    "x": "z",
    "e": "w",
    "s": "a",
    "z": ",",
    "Z": "<",
    "a": ";",
    "A": ":",
    "q": "[",
    "Q": "{",
    " ": " ",
}

function convertShiftedRightToCorrect(myShiftedString) {
    arrayHolderChar = []
    for (i = 0; i <= myShiftedString.length - 1; i++) {
        // console.log(myString[i])
        if (myShiftedString[i] == myShiftedString[i].toUpperCase() && ![";", "{", "[", ":", "<", ",", " "].includes(myShiftedString[i])) {
            isUpperCase = true
        } else {
            isUpperCase = false
        }

        let myStringLower = myShiftedString[i].toLowerCase()

        convertedString = mapDictionaryConverstion[myStringLower]

        if (isUpperCase) {
            convertedString = convertedString.toUpperCase()
        }

        arrayHolderChar.push(convertedString)
    }

    return arrayHolderChar.join("")
}


let myShiftedString = "Jr;;p ept;f"
convertShiftedRightToCorrect(myShiftedString)

myShiftedString = "Lmiyj od ,u jrtp"
convertShiftedRightToCorrect(myShiftedString)

// first we try to solve in a dumb way that works


// --------------------------------------------------------------------------------------------- //


















