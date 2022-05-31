// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30456894#overview
// ownership

// we use rustc main.rs to compile the rust code
// then it generates an executable
fn main(){
    let var = 1;
    // this is i32, it has fixed size, so it goes to the stack

    let mut s = "Hello".to_string(); // this will be created on the heap
    // because it is is variable in size

    s.push_str(", world"); // we can include this to s
    // because s is allocated on the heap, so it can grow

    


}













