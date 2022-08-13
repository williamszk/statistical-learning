fn main() {
    // start the same tutorial at:
    // https://youtu.be/ygL_xcavzQ4?t=1971

    // about arrays
    let arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    println!("1st: {}", arr_1[0]);

    // get length of the array
    println!("Length: {}", arr_1.len());

    // loop through array
    let mut loop_idx = 0;
    loop {
        if arr_1[loop_idx] % 2 == 0 {
            loop_idx += 1;
            continue;
        }
        if arr_1[loop_idx] == 9 {
            break;
        }
        println!("Val: {}", arr_1[loop_idx]);
        loop_idx += 1;
    }
}
// Stopped at:
// https://youtu.be/ygL_xcavzQ4?t=2243