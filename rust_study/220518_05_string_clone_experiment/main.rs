// a string is of variable length
// so it is stored in the heap
// hence there is not implicit copying (clone)
// let's experiment with it
// the string will behave like the vector

fn main(){
    let mut s = "Hello".to_string();
    // notice that we are using the keyword mut
    // so that we can change the s object

    s.push_str(", world");

    println!("{}", s);

    let y = s;
    // println!("{}", s); // this will break
    println!("{}", y); // this doesn't break

    // s.push_str(" again"); // this will break
    // y.push_str(" again"); // this will break because y is not mutable

    let mut z = y;
    // println!("{}", y); // this will break
    println!("{}", z); // this doesn't break

    z.push_str(" again"); // this doesn't break
    println!("{}", z);

    // use clone to verify that it works
    let m = z.clone();
    println!("z = {}", z);
    println!("m = {}", m);

    // we can also alter z
    // given that it is mutable and it was cloned to m
    z.push_str(" I say");
    println!("z = {}", z);
    println!("m = {}", m);
    // m is not altered

    // what happens when we define a string as not mutable?
    // does it make an implicit copy? or do we need to use clone?

    let a = "Hi".to_string();
    // is "a" on the heap or stack?
    // an object should be in the stack when its size is fixed
    // an object should be in the heap when it size is mutable

    let b = a;
    // is this borrowing? or implicit copy?

    // println!("a = {}", a); // this will break
    // a is still in the heap
    // although a is of fixed size...
    


}