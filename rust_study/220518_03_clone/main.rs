fn main(){
    let x = vec!["tyler".to_string()];
    let y = x.clone(); 
    // we can perform a "clone" which is a deep copy

    println!("x = {:?}", x);
    println!("y = {:?}", y);
    // we don't find errors anymore
}