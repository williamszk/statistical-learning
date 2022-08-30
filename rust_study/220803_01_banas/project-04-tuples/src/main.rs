fn main() {
    println!("Hello, world!");

    let my_tuple: (u8, String, f64) = (29, "William".to_string(), 50_000.00);


    println!("{:?}", my_tuple);

    println!("Name: {}", my_tuple.1);

    let (v1, v2, v3) = my_tuple;

    println!("Age: {}", v1);
    println!("Name: {}", v2);
    println!("Bank Account: ${:.2}", v3);
}
