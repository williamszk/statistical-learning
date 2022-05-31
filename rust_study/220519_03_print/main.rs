// https://www.udemy.com/course/rustaceans/learn/lecture/19055562#overview

fn main() {
    // string formating
    println!("My name is {} and I'm {} years old", "Bob", 28);

    // expressions
    println!("a + b = {}", 1 + 2);

    // using argument with position
    // positional argument
    println!("{0} has a {2} and {2} has a {1}", "Bob", "Rat", "Cat");

    // we can also use named argument
    println!("{name} {surname}", surname = "Rambo", name = "Bob");

    // print traits
    println!("binary: {:b}\thex: {:x}\toctal: {:o}", 50, 50, 50);

    // debug print
    // an array is not convertible to array
    // but rust can convert it into a printable format
    println!("Array: {:?}", [1, 2, 3]);
    // println!("A test print array: {}", [1, 2, 3]); // this will give error
}
