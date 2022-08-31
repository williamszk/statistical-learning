// https://www.udemy.com/course/rust-programming-the-complete-guide/learn/lecture/30457070#overview

fn main(){
    let s = String::from("takes");

    takes_ownership(s); // gives ownership of "s"'s value to the function

    // println!("{}", s); // this will break
    // because we have ownership of the variable s to the function

    let val = 1;
    make_copy(val); // this function makes a copy of val
    // it does not take ownership
    // an i32 implements the copy trait
    println!("{}", val);
    // string does not implment the copy trait


    let str1:String = give_ownership();
    // when we call the function we pass the ownership of the value
    // to the object str1
    println!("{}", str1);


    let str_in_1 = "Hi there!".to_string(); // create variable here
    let str_out: String = take_and_give_ownership(str_in_1); // pass ownership to function
    // then function pass ownership to the str_out
    println!("{}", str_out); // this doesn't break
    // println!("{}", str_in_1); // this will break
    // because str_in_1 passed the ownership to the function right after
    


}

fn takes_ownership(s: String){
    let s2 = s;
    println!("{}", s2);
}

fn make_copy(num: i32){
    let val1 = num;
    println!("{}", val1);
}

fn give_ownership() -> String {
    // aparently there is no return in rust
    // and we don't use ; at the end of the return

    "given".to_string() // the function owns the "given"
}

fn take_and_give_ownership(my_str:String) -> String {
    my_str
}