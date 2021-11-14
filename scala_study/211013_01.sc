// https://rockthejvm.com/courses/728053/lectures/13122607

// set PATH=%PATH%;C:\Users\william.suzuki\null\Coursier\data\bin
// scala3-repl.bat


// class and instance
class Animal {
    val age: Int = 0
    def eat(): Unit = println("I am eating")
}

val anAnimal = new Animal
anAnimal.age
anAnimal.eat()
// inheritance
class Dog(val name: String) extends Animal {
    // Animal is the superclass
    // constructor definition
    // constructor argument name
    // like attribute in Python in __init__
    // put a val before the constructor definition
    // so it becomes a member of the class

    // age is a field of Animal an hence Dog
    // constructor arguments are not fields

}


val aDog = new Dog("Lassie")
aDog.age
aDog.eat()
aDog.name

// subtype polymorphism
val aDeclaredAnimal: Animal = new Dog("Hachi")
aDeclaredAnimal.eat() // this comes from the Dog class before the Animal
// the most derived class will be called first

// abstract class
abstract class WalkingAnimal {
    val hasLegs = true
    def walk(): Unit
    // private val hasLegs = true
    // protected val hasLegs = true
    // private makes the field only accessible by the class
    // protected makes the field only accessible by its descendents
    // we can define a function walk() inside the abstract class without 
    // writing any implementation, this will signal to the descedents
    // classes that they need to implement the walk() function
}

// def write(): Unit
// Declaration of method write not allowed here: only classes can have declared but undefined members

class Cat extends WalkingAnimal {
    def walk(): Unit = {
        println("The cat is walking.")
    }
}

// an expression is some piece of code that evaluates to some value
val someValue = {
    val a = 1 + 1
    val b = 2 + 2
    // this is a code block
    // in Scala a codeblock is also an expression
    // in the sense that it reduces to a value

    b
}

val aValue2 = {
    val a = 2 + 2
    val b = 3 + 4
    // in a code block if there is no last expression
    // the entire codeblock evaluates to Unit
    // which is equivalent to None in python
}

val aCat = new Cat
aCat.walk()
// Interface = ultimate abstract type
trait Carnivore {
    def eat(animal: Animal): Unit
}


class Crocodile extends Carnivore {
    def eat(animal: Animal): Unit = {
        println(s"The Crocodile is eating $animal.name")
    }
}

val bobTheCrocodile = new Crocodile
bobTheCrocodile.eat(aDeclaredAnimal)





