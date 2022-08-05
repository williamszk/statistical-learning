object Expressions extends App {
  
    val x = 1 + 2 // expression
    println(x)

    println(x == 1)
    println(x != 1)
    // unary operator, it only needs 1 parameter
    println(!(x != 1))


    // statements vs expression 
    // statements == instructions

    // statemtns -> None/Nil

    // If-statement
    // If-expression

    val aVal01 = if (1 == 1) 5 else 3
    println(aVal01)

    // we should not use loops in Scala

    var i = 0
    while (i < 10) {
        println(i)
        i += 1
    }
    // this is imperative code
    var avar02: Int = 0
    val aWeird = (avar02 = 3) // type is Unit (void)
    println(aWeird.getClass()) // void
    println(aWeird) // () 
    // () this is the Unit or void

    // side effects: prinln(), while, reassignment

    val aCodeBlock = {
        val y = 2
        if (y > 3) "hi" else "bye"
    }

    println(aCodeBlock)

}
