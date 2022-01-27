fn main() {
    println!("Hello, world!");

    let x: u64 = 45;
    let f: f64 = 6.7;
    let b: bool = false;

    println!("Just print those guys: {} {} {}", x, f, b);

    let n = 45;

    if n < 30 {
        println!("The number is less than 30");
    } else if n > 50 {
        println!("The number is greater than 30");
    } else {
        println!("I don't know!");
    }


}
// https://www.youtube.com/watch?v=RBo8Vcbpc4o&ab_channel=dcode