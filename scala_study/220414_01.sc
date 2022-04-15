// https://www.udemy.com/course/rock-the-jvm-scala-for-beginners/learn/lecture/7660550#overview
// use this command in the terminal to run the scala interactive terminal
// scala3-repl.bat

// it is similar to Go in the sense that the type comes after
val x: Int = 42
println(x)
// like Go we don't need ; at the end of the line

// Interstingly Scala is a compiled language although it has a REPL
// Or Scala is  JIT language?

x = 2
// scala> x = 2
// -- Error:
// 1 |x = 2
//   |^^^^^
//   |Reassignment to val x

// val creates a constant object, we can't change its content
// VAL are immutable
// it is like const in javascript
// or final

val y = 54
// scala> val y = 54
// val y: Int = 54

// Scala does type inferencing
// like in Go
// we don't need to declare the type of all variables

val x1:Int = "Hello"
// scala> val x1:Int = "Hello"
// -- Error:
// 1 |val x1:Int = "Hello"
//   |             ^^^^^^^
//   |             Found:    ("Hello" : String)
//   |             Required: Int

// The compiler will not like this







































