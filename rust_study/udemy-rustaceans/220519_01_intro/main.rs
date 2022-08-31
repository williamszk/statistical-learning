use std::io;

fn main(){
    println!("Hello World");

    let mut input:String = String::new();

    println!("This is just a test: {}", 1 + 1);
    println!("Say something:");
    // when there is a exclamation mark we say that it is a macro
    
    

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            println!("You said: {}", input);
        },
        Err(e) => {
            println!("Something went wrong: {}", e);
        }
    }
}