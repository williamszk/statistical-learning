// https://youtu.be/ygL_xcavzQ4?t=2236

fn main() {
    let arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    println!("1st: {}", arr_1[0]);

    // we need to use {:?} so that we can print a
    // collection type
    println!("{:?}", arr_1);

    let mut idx = 0;
    while idx < arr_1.len() {
        println!("Arr : {}", arr_1[idx]);

        idx += 1;
    }

    println!("==================================");

    for val in arr_1.iter() {

        println!("Val : {}", val);

    }
}


// next tuples:
// https://youtu.be/ygL_xcavzQ4?t=2360