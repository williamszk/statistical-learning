// to start the scala repl
// scala3-repl.bat

// https://rockthejvm.com/courses/728053/lectures/13122611

val meaningOfLife: Int = 42

val aBoolean = false

// Int, Boolean, Char, Double, Float, String

val aString = "I love Scala"

val aComposedString = aString + " and I love JavaScript"

// interpolated strings, or format string
val anInterpolatedString = s"The meaning of life is $meaningOfLife"

// values and expressions
// expressions := structures that can be reduced to a value
val anExpression = 2 + 3

// if-expression
// in other languages we have if-statements
// but in scala we have if expressions
val ifExpression = if (meaningOfLife > 43) 56 else 999
// this is similar to the ternary operator

val chainedIfExpression = 
    if (meaningOfLife > 43) 56
    else if (meaningOfLife < 0) -2
    else if (meaningOfLife > 999) 78
    else 0

// code block
val aCodeBlock = {
    val aLocalValue = 67

    aLocalValue + meaningOfLife
}

// what is the difference between a code block and a function?

def myFunction(x: Int, y: String): String = {
    s"$x " + y
}

myFunction(1, "is not even.")

// define a factorial function
def factorial(n: Int): Int = {
    if (n == 1) 1
    else if (n > 1) {
        factorial(n-1) * n
    } else {
        -1
    }
}

factorial(4)
factorial(5)
factorial(6)

// In scala we don't use loops nor iteration, we use recursion.

println() // is an example of a function that returns Unit, which equivalent to void, None or Nil

def myUnitReturningFunction(): Unit {
    println("I don't love to returning Unit")
}

// a function that returns Unit is an expression?
// Yes, and it is not a statement, because it returns something

val aUnitInstance = ()

// next class is:
// https://rockthejvm.com/courses/728053/lectures/13122607









