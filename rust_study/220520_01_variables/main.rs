// https://www.udemy.com/course/rustaceans/learn/lecture/19054634#overview

// this is lint, for the case where we allow unused variables
#[allow(unused_variables)]
#[allow(unused_mut)]

fn main() {
    let name = "Bob";
    let age = 29;

    let amount: i64 = 9223372036854775807; // this is the max value for i64
    println!("{}", amount);

    // by default the integer is going to be an i32

    // rust follows snake case for variables
    // age = 76; // this will give error, because variables in rust are imutable by default

    let mut length = 44;

    // shadowing is allowed
    let color = "Blue";
    let color = "Red";
    // we can redeclare the variable... this is shadowing
    println!("Color is {}", color);
    // strings must be in double quotes

    let color = 87;
    println!("Color is {}", color);
    // we can even assign the variable to a different type

    // declare multiple variables simultaneously
    let (a, b, c) = (2, 3, 4);
    let (a, b, c) = (2, true, "Red");
    // we can use shadowing with multiple assignment

    

}
