// https://www.udemy.com/course/rustaceans/learn/lecture/19082244#overview

fn main() {
    // for loop
    for i in 1..6 {
        say_hi();
    }

    say_hello("Bob!");

    let mut bob_name = "Bob";
    println!("bob_name: {}", bob_name);
    say_hello_to_alex(&mut bob_name);
    println!("bob_name: {}", bob_name);

    let greeting = create_greeting(&mut bob_name);
    println!("greeting: {}", greeting);

}

fn say_hi() {
    println!("Hello there!");
}

// passing argument to functions
// passing by value or
// passing by reference

// in rust we pass values as borrowing

fn say_hello(name: &str) {
    println!("Hello {}", name);
}

// we can pass the variable by reference 
// we can modify the valu inside the function
fn say_hello_to_alex(name: &mut &str){
    //! This function will take the name variable
    //! and modify it to Alex
    *name = "Alex";
    println!("Hello {}", name);
}

fn create_greeting(name: &mut &str) -> String {
    let greeting = format!("Hello {}", name);
    return greeting;
}


