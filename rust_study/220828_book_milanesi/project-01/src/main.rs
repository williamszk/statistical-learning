fn main() {
    println!("Hello, world!");

    println!(
        "{}",
        &"This \
                    is \
                    just \
                    one \
                    line. \
    "
    );

    println!(
        "{}",
        "These\n\
                    are\n\
                    three lines"
    );

    // about the terms:
    // declaration
    // initialization
    // variable
    // object
    // identifier
    // alias

    // in here we just declare a var01;
    // if the declare a variable we need to set its type
    // so that the program can allocate enough memory for it
    let var01: u32;

    // in here we are assigning a value to the variable
    var01 = 122;

    println!("{}", var01);

    // the variable var01 is not an alias to 122
    // the variable var01 is an identifier to the object
    // an object is a space in memory
    // we can change the content of the space in memory

    // when we reserve space in memory for an object
    // we say that we are allocating space in memory
    // when we remove this reservation we say that we are 
    // deallocating space in memory

    // in C and C++, or other languages
    // many variables can be associated with the same space in memory
    // (is this correct?)
    // 




}
