fn main() {
    // 1 1 2 3 5 8 13 21 34 55 89 144
    // 0 1 2 3 4 5  6  7  8  9 10  11
    // let answer = fib(6);
    // println!("{:}: this should be 13", answer);
    // let answer = fib(10);
    // println!("{:}: this should be 89", answer);
    // let answer = fib(9);
    // println!("{:}: this should be 55", answer);
    // let answer = fib(11);
    // println!("{:}: this should be 144", answer);

    // real test
    let answer = fib(40);
    println!("{:}", answer);
}

fn fib(idx: i32) -> i32 {
    if idx == 0 {
        return 1;
    } else if idx == 1 {
        return 1;
    } else {
        let mut val_t_2 = 1;
        let mut val_t_1 = 1;
        let mut cur = 0;
        for _ in 2..=idx {
            cur = val_t_2 + val_t_1;
            val_t_2 = val_t_1;
            val_t_1 = cur;
        }
        return cur;
    }
}
