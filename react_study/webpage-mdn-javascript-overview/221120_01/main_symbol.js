// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol

Symbol('a')
Symbol(10)
Symbol(undefined)

Symbol(10n)

const sym1 = Symbol()
const sym2 = Symbol('foo')
const sym3 = Symbol('foo')

sym3 === sym2 // false
sym2 === sym2 // true

// how to extract the description out of the symbol

Symbol(1) === Symbol(1) // false
// the argument inside the Symbol constructor is a description

const sym = Symbol('foo')
typeof sym // "symbol"
const symObj = Object(sym)
typeof symObj // "object"
symObj // [Symbol: Symbol[foo]]

sym.valueOf()
sym

sym.valueOf() === sym

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/valueOf
symObj === sym // false
symObj.valueOf() === sym // true

const sym4 = Symbol('example')
sym4 === sym4.valueOf() // true
