#![allow(unused)]

use rand::Rng;
use std::cmp::Ordering;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, ErrorKind, Write};

fn main() {
    println!("Hello, world!");
    // macros uses ! in its name
    println!("What is your name?");
    let mut name = String::new();
    let greeting = "Nice to meet you.";
    io::stdin()
        .read_line(&mut name)
        .expect("Didn't receive input");

    println!("Hello {}! {}", name.trim_end(), greeting);

    const ONE_MIL: u32 = 1_000_000;
    const PI: f32 = 3.141592;
    let age = "47";
    let mut age: u32 = age.trim().parse().expect("Age wasn't asssigned a number");
    // we can create variables with the same name, but with different
    // data types, this is called shadowing
    age = age + 1;

    println!("I'm {} and I want ${}", age, ONE_MIL);

    println!("Max u32: {}", u32::MAX);
    println!("Max u64: {}", u64::MAX);
    println!("Max u128: {}", u128::MAX);
    println!("Max f32: {}", f32::MAX);
    println!("Max f64: {}", f64::MAX);
    println!("Max usize: {}", usize::MAX);

    let is_running = true;
    let my_grade = 'A';

    let random_num = rand::thread_rng().gen_range(1..101);
    println!("Random: {}", random_num);

    age = 8;
    if (age >= 1) && (age <= 18) {
        println!("You have an important birthday");
    } else if (age == 21) || (age == 50) {
        println!("You have an important birthday");
    } else if age >= 65 {
        println!("You have an important birthday");
    } else {
        println!("You have an NOT important birthday");
    }

    // ternary operator
    let mut my_age = 47;
    let can_vote = if my_age >= 18 { true } else { false };

    println!("Can vote: {}", can_vote);

    // match, it is like switch
    let age2 = 19;
    match age2 {
        // this will go from 1 to 18 included
        1..=18 => println!("You have an important birthday"),
        21 | 51 => println!("You have an important birthday"),
        65..=i32::MAX => println!("You have an important birthday"),
        _ => println!("You have an NOT important birthday"),
    };

    // match is an statement it does not return anything

    // another possibility that we can work with
    let my_age = 18;
    let voting_age = 18;
    match my_age.cmp(&voting_age) {
        Ordering::Less => println!("Can't vote"),
        Ordering::Greater => println!("Can vote"),
        Ordering::Equal => println!("You gained the right to vote"),
    };


}

// https://youtu.be/ygL_xcavzQ4?t=1452

// Stoped at:
