// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30456894#overview
// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30456980#overview
// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30457024#overview
fn main() {
    // stack: store variables
    //  pushing and getting data to the stack is faster
    // heap: store variables

    // each value has its owner
    // when owner goes out of scope, the value is dropped
    // the value is freed

    // by default var is i32
    // var will be created on the stack
    let var = 1;
    println!("{:?}", var);
    // s will be created on the heap
    // because it is mutable
    let mut s = "hello".to_string();

    s.push_str(", world!");
    // we can append values to the heap because
    // s is on the heap, and in the heap values can grow

    // move
    let x = vec!["tyler".to_string()];
    let y = x;
    // this will error because y is the owner of the value
    // println!("{:?}", x);

    let z = y;
    // this will error because the value of y is owned
    // by z
    // println!("{:?}", y);
    println!("{:?}", z);

    // everytime we assign a value of one variable
    // to another we are changing ownership of the value
    // and we are moving its value

    // note that here we are using clone
    let x1 = vec!["tyler".to_string()];
    let x2 = x1.clone();
    println!("x2: {:?}", x2);
    println!("x1: {:?}", x1);
    // now both x1 and x2 have the value
}

// to compile:
// rustc main.rs
// to run the code:
// ./main
