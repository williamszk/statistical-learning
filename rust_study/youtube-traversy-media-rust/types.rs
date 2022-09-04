pub fn run(){
    // default i32
    let x = 1;

    // default f64
    let y = 2.14;

    // add explicit type
    let z: i64 = 7364928374;

    // find max size 
    println!("Max i32: {}", std::i32::MAX);
    println!("Max i64: {}", std::i64::MAX);
    println!("Max f64: {}", std::f64::MAX);
    println!("Min f64: {}", std::f64::MIN);

    // Boolean
    let is_active = true;

    // get boolean from expression
    let is_greater = 10 < 5;

    // char

    let a1 = 'a';
    let a2 = "abc";
    let face = '\u{1F600}';

    

    println!("{:?}",(x,y,z,is_active, is_greater, a1, a2, face));




}