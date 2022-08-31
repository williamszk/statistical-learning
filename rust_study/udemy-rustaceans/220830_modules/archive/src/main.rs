use crate::archive::arch::archive_file;

// we can give an alias to a function too...
use crate::archive::arch::archive_file_with_a_long_name as arc;

// Random number generator
// using external crates
use rand::Rng;

mod archive;

fn main() {
    println!("Hello, world!");

    archive_file("my-diary.txt");

    arc("Long ass namek for a file.txt");

    let mut rng = rand::thread_rng();

    // I think his will generate an unbounded i32
    let a: i32 = rng.gen();

    println!("My random number {}", a);

    // generate an integer in a bounded range
    let my_rand_01 = rng.gen_range(0, 100);

    println!("My random number: {}", my_rand_01);

    // generate a bounded float
    let my_bouded_float = rng.gen_range(0.0, 90.00);
    println!("My random float number: {}", my_bouded_float);

    // generate random string
    let rand_string: String = rand::thread_rng()
        .sample_iter(&rand::distributions::Alphanumeric)
        .take(100)
        .collect();

    println!("A random string: {}", rand_string);
}
