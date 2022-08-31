// https://youtu.be/ygL_xcavzQ4?t=2489

fn main() {
    // two types of strings

    // String
    // &str

    let mut st1 = String::new();

    st1.push('A');

    st1.push_str(" word");

    st1.push_str(" about love and peace");

    println!("{}", st1);


    // split string into words
    for word in st1.split_whitespace(){
        println!("{}", word);
    }


    // replace string
    let st2 = st1.replace("A", "Another");
    println!("{}", st1);
    println!("{}", st2);


    // string of random characters
    let st3 = String::from("x r t b h k k a m c");

    let mut v4: Vec<char> = st3.chars().collect();

    // sort characters
    v4.sort();

    // remove duplicates
    v4.dedup();

    for char in v4 {
        println!("{}", char);
    }

    // &str is a stack allocated string

    // String is a heap allocated string, it is changeable

    let st4: &str = "Random String";

    let mut st5: String = st4.to_string();

    println!("{}", st4);

    // rust accepts unicode
    st5.push_str(" an addition 😊");

    println!("{}", st5);

    // transform the string into an array of bytes
    let byte_arr_1 = st5.as_bytes();

    println!("{:?}", byte_arr_1);

    // get a slice of the array
    let st6 = &st5[0..6];
    println!("{}", st6);

    // get string length
    println!("Length of string: {}", st6.len());

    // delete all content of a String
    st5.clear();
    println!("{}", st5);

    // notice that we declared st6 again here
    let st6 = String::from("Just some");
    let st7 = String::from(" words");

    let st8 = st6 + &st7;

    for char in st8.bytes(){
        println!("{}", char);
    }


}

// Next tutorial about casting
// https://youtu.be/ygL_xcavzQ4?t=3023 