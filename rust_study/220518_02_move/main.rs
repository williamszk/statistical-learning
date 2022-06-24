// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30456980#overview

fn main(){
    let x = vec!["tyler".to_string()];
    let y = x; // this is called a move
    // x does not owns any value
    // y owns the value
    // println!("{:?}", x); // this will give error
    println!("{:?}", y);

    // move the ownership from y to z
    let z = y;
    // println!("{:?}", y); // this gives error
    println!("{:?}", z);
    // I didn't understand why this should be considered bad...

    // println!("{:?}", x); // we can't use x anymore
}