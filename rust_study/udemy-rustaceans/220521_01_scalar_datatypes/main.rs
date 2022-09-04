// https://www.udemy.com/course/rustaceans/learn/lecture/19054636#overview

fn main() {

    // i8   u8 
    // i16  u16
    // i32  u32 <- this is the default
    // i64  u64
    // i128 u128

    // float types
    // f32 
    // f64 <- this is the default

    let pi: f32 = 4.0; // we need to include the zero at the end

    // number separators
    let million = 1_000_000;
    let random = 3_897.45_0982;

    // booleans
    let is_day = true;
    let is_night = false;

    // chars
    let char1 = 'A';
    let smiley_face = '\u{1f601}'; // 😁 

    println!("{}", smiley_face);

    // the code in rust only accepts ascii characters or can we 
    // write unicode in the rust code? yes, I think we can include unicode in rust code
    // can we set unicode as variables?

    // let 🙂 = "Smiley Face";
    // println!("{}", 🙂);
    // this will give errors, we can't use emojis as identifiers of variables





}


