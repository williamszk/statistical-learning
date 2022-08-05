object ValuesVariablesTypes extends App {
  val x: Int = 10
  println(x)

  // val are immutable
  // x = 3

  // the compiler can infer types
  val y = 13
  println(y)

  val myString: String = "Hello from Scala"

  println(myString)
  // there is no need fro semi-colon in Scala

  val anotherString = "goodbye" 
  println(anotherString)

  val aBoolean: Boolean = false
  println(aBoolean)

  val aChar: Char = 'A'
  println(aChar)

  val anInt: Int = x
  // val aShort: Short = 4716233323
  val aShort: Short = 4613
  // Short: 4 bytes: 32 bits
  // val aLong: Long = 9999999999
  val aLong: Long = 99999999L
  // Like in Java we include an L at the end of a Long number
  // Long: 8 bytes: 64 bits

  val aFloat: Float = 10.123f
  // consistent with Java syntax 
  val aDouble: Double = 3.14

  // Variables
  var aVariable: Int = 4
  // Side effects

}
