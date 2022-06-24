// https://www.udemy.com/course/rustaceans/learn/lecture/19054640#overview


#[allow(unused_variables)]


fn main() {
    // strings are slices
    let cat: &str = "Fluffy";

    // lifespan
    let cat: &'static str = "Fluffy";

    println!("{}", cat);

    // string slices are immutable

    // there is also the String object
    // which is different from the string slice
    // the String object is modifiable

    let dog = String::new();

    // we can create a String object from a string slice
    let dog = String::from("Ruppert");

    println!("{}", dog);

    // format macro
    // similar to the println macro
    // but format will create a new string, instead of printing to the console
    let owner = format!("Hi I'm the owner of {}", dog);
    println!("{}", owner);

    // get the length of the string
    println!("{}", dog.len());
    
    // methods that work on String object
    // not string slice

    let mut dog = String::from("Ruppert");

    dog.push(' ');
    dog.push_str("the dog");
    println!("{}", dog);

    let new_dog = dog.replace("the", "is my");
    println!("{}", new_dog);








}