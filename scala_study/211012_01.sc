// https://www.udemy.com/course/rock-the-jvm-scala-for-beginners/learn/lecture/10373000#overview
// set PATH=%PATH%;C:\Users\william.suzuki\null\Coursier\data\bin
// scala3-repl.bat

// https://rockthejvm.com/

// https://rockthejvm.com/courses/728053/lectures/13122825
// https://github.com/rockthejvm

// https://github.com/rockthejvm/scala-at-light-speed

val meaningOfLife: Int = 42

// val is a constant
// const int meaningOfLife = 42;

// illegal:
// meaningOfLife = 50

val aBoolean = false
// most of the time, type mensioning is optional

// Int, Boolean, Char, Double, Float, String

val aString : String = "I love Scala!"
val aComposeString = "I" + " " + "live" + " " + "Scala"

// a format string, like a f-string in Python
val anInterpolatedString = s"The meaning of life is $meaningOfLife"

// expressions
val anExpression = 2 + 3
// expression are structures that can be reduced to a value

// if-expression
val ifExpression = if (meaningOfLife > 42) 56 else 999
// this is like the ternary operator

val chainedIfExpression = 
    if (meaningOfLife > 42) 56
    else if (meaningOfLife < 0) -2
    else if (meaningOfLife > 999) 78
    else 0
// this is not possible in Python
// we assign values depending on some conditions
// in Python the idea is to do something given some 
// conditions

// code block 
// in Scala a codeblock is also an expression
// in the sense that it reduces to a value

val aCodeBlock = {
    // definitions
    val aLocalValue = 67

    // the last expression is the value of the value
    // aCodeBlock
    aLocalValue + 3
}

// define a function
def myFunction(x: Int, y: String): String = {
    y + " " + x
}

myFunction(10, "Hello")

// recursive functions
def factorial(n: Int): Int = {
    if (n <= 1) 1
    else n * factorial(n-1)
}

factorial(4)
factorial(5)

// In scala we don't use loops 
// or iteration
// we use recursion

// the Unit type = no meaningful value === void, None, 
println("I love scala!")
// this function returns a Unit type
// this is related to SIDE EFFECTS

def myUnitReturningFunction(): Unit = {
    val someValue = 1 + 1
}

val myOutput = myUnitReturningFunction()
val myOutput = "Unit"
val myOutput = 10
// we can redefine the value of a value (not a variable)

// we can represent the Unit if ()
val theUnit = ()



// https://rockthejvm.com/courses/728053/lectures/13122607


