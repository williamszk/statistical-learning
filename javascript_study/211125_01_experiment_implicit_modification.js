


myObject1 = {
    a: 1,
    b: 2,
    c: 3
}


function myImplicitModification(myObject){
    myObject.a = 10
    return null
}

console.log("myObjec1 before the modification")
console.log(myObject1)

myImplicitModification(myObject1)

console.log("myObject1 after the modification")
console.log(myObject1)




