
fn main() {
    println!("Hello, world!");

    let var = 1; // this is created on the stack
    println!("{}", var);

    let mut mystring = "hello".to_string(); // this is going to be created on the heap
    mystring.push_str(", world");
    println!("{}", mystring);

    let my_vec = vec!["bill".to_string()];
    let my_vec2 = my_vec;
    // println!("{:?}", my_vec); // this is a violation of the ownership rule
    let my_vec3 = my_vec2;
    // println!("{:?}", my_vec2); // this is a violation of the ownership rule
    println!("{:?}", my_vec3);

    // Clone, this is a deep copy of a string
    // if the vector is large, then this can be an expansive operation
    let my_vec1_1 = vec!["Ken".to_string(), "Thompson".to_string()];
    let my_vec1_2 = my_vec1_1.clone();
    let my_vec1_3 = my_vec1_2.clone();
    println!("{:?}", my_vec1_1);
    println!("{:?}", my_vec1_2);
    println!("{:?}", my_vec1_3);

    // About copy
    let var01 = 1;
    let var02 = var01;
    println!("var01 = {}, var02 = {}", var01, var02);
    // There is no problem running this example, there is an implicit copy in the case of i32
    // simpler datatype like int, float, chars implement copy, which will clone values by default

    // But more complex objects will implement moves, which will invalidate the previous variable
    // in this case if can use the clone() method

    let my_string = String::from("takes");

    takes_ownership(my_string);

    // println!("{}", my_string); // this will give an error
    let my_2_string = String::from("takes");
    clones_value(my_2_string);

    // println!("{}", my_2_string); // this will give an error

    let my_3_string = String::from("takes3");
    clones_value(my_3_string.clone()); // here we clone the argument right when pass it in the receiver
    println!("{}", my_3_string);

    // we can reuse the my_3_string in other places
    takes_ownership(my_3_string.clone()); // this is also ok
    println!("{}", my_3_string);
    // when we pass an object to a function, the function takes the ownership of its content
    // but this can be mitigated if we pass the object cloning it at the same time
    // this is like passing by value
    // unlike Python we can't just pass by reference, because in Rust the value of the object
    // will be taken from the previous object and given to another object


    // this is an exaple where we give the ownership of a value from
    // a function to a variable
    let my_given_str = gives_ownership();
    println!("{}", my_given_str);

    // build a function that takes and gives the value of a variable 
    // to another variable
    let my_to_give_str = "I'll be given to another variable".to_string();
    let my_to_receive_str = takes_and_gives_ownership(my_to_give_str);
    println!("{}", my_to_receive_str);
    // println!("{}", my_to_give_str); // this gives error because it was given 
    // to the function takes_and_gives_ownership

    // references
    // type: shared, mutable


}
// after the end of the main function
// var is dropped and mystring is dropped

fn takes_ownership(a_string: String){
    let my_string2 = a_string;
    println!("takes_ownership: {}", my_string2);
}

fn clones_value(a_string: String) {
    let my_string2 = a_string.clone();
    println!("clone_value: {}", my_string2);
}

fn gives_ownership() -> String {
    "given".to_string()
}

fn takes_and_gives_ownership(a_str: String) -> String {
    a_str
}


// Create a function that takes one argument called val that is of type Vec with the values: 
// 1,3,5,7. Inside of this function check the first value of the vector and see if it is equal 
// to one. If the value is equal to one, then return true, otherwise return false. Next add the 
// value 15 to the vector. Print out the vector to confirm your results.


// Create a function called "add_two". This function is going to take one parameter that is i8 and 
// add two to it. For the function, do you have to pass the value by reference in order for you to 
// maintain ownership of it inside of main?

