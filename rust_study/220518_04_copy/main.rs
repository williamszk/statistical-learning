// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30457064#overview

fn main(){
    let x = 1;
    let y = x; 
    // when we run here, we are implicitly applying a copy
    // instead of a "move", which would happen with objects store in the stack
    // so there is no need to clone
    // the implicity copy (clone="deepcopy") happens when the object
    // is store in the stack
    // and a object is stored in the stack when its size is fixed


    println!("x = {}, y = {}", x, y);
    // here we can use x and y,
    // in the previous example we couldn't because
    // x was a vector, a collection of datatypes

    // x = 2; // this will give error because in rust
    // let is a const
    println!("x = {}, y = {}", x, y);
    
}

// a string is of variable length
// so it is stored in the heap
// hence there is not implicit copying (clone)
// let's experiment with it
// the string will behave like the vector
