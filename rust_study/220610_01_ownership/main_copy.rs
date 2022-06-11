// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30457064#overview

fn main() {
    // about copy
    let x = 1;
    let y = x;
    // when he value is elementar it is automatically copied
    // we don't need to use clone

    // the compound types implement a move() which means that
    // the value moves from one variable to another

    // in copy, there is not move just an implicit clone

    println!("x = {}, y = {}", x, y);

    let s = String::from("takes");
    let my_str_2 = "Mike".to_string();
    println!("my_str_2: {}", my_str_2);
    takes_ownership(s); // s is now owned by s2 inside the function...

    // so we can't print the value of s in here given that s lost its ownership
    // println!("s: {}", s); // this will break

    // we can pass the value cloning it, like passing by value
    // instead of passing by reference
    takes_ownership(my_str_2.clone());
    println!("my_str_2: {}", my_str_2); // this will work

    let num = 10;
    takes_a_copy(num);
    println!("num: {}", num);

    let str1: String = give_ownership();
    println!("str1: {}", str1);

    let my_str_3 = String::from("Bobson");
    let my_str_4: String = take_and_give(my_str_3);
    // println!("my_str_3: {}", my_str_3);
    println!("my_str_4: {}", my_str_4);

    let cond = true;
    if cond {
        let str4 = my_str_4;
        println!("str4: {}", str4);
    } else {
        let _str5 = my_str_4;
    }

    // println!("my_str_3: {}", my_str_3); // this will give error
    // println!("str4: {}", str4);
}

fn take_and_give(s: String) -> String {
    s
}

fn give_ownership() -> String {
    "given".to_string()
}

fn takes_ownership(s: String) {
    let s2 = s;
    println!("s2: {}", s2);
}

fn takes_a_copy(num: i32) {
    let num2 = num;
    println!("num2: {}", num2);
}
