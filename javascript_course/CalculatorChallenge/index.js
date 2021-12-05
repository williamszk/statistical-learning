
let num1 = document.getElementById("num1")
let num2 = document.getElementById("num2")
let num3 = document.getElementById("result")

num1.textContent = "2"
num2.textContent = "3"

setInitialValueResult()

num1Int = parseInt(num1.textContent, 10) 
num2Int = parseInt(num2.textContent, 10)

function setInitialValueResult(){
    num3.textContent = "Result: "
}

function add(){    
    setInitialValueResult()    
    let sumInt = num1Int + num2Int
    num3.textContent += sumInt.toString()
}

function subtract(){
    setInitialValueResult()
    let sumInt = num1Int - num2Int
    num3.textContent += sumInt.toString()
}

function multiply(){
    setInitialValueResult()
    let sumInt = num1Int*num2Int
    num3.textContent += sumInt.toString()
}

function divide(){
    setInitialValueResult()
    let sumInt = num1Int/num2Int
    num3.textContent += sumInt.toString()
}

