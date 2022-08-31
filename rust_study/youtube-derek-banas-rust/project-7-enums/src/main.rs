fn main() {
    //  https://youtu.be/ygL_xcavzQ4?t=3127
    println!("Hello, world!");

    enum Days {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday,
    }

    impl Days {
        fn is_weekend(&self) -> bool {

            match self {
                Days::Saturday | Days::Sunday => true,
                _ => false
            }
        }
    }


    let today:Days = Days::Monday;

    match today {
        Days::Monday => println!("Everyone hates monday"),
        Days::Tuesday=> println!("It is donut day"),
        Days::Wednesday => println!("Hump day"),
        Days::Thursday => println!("Pay day"),
        Days::Friday => println!("Almost weekend"),
        Days::Saturday => println!("Weekend"),
        Days::Sunday => println!("Weekend"),
    }


    println!("Is today the weekend: {}", today.is_weekend());

}

// Next video Vectors:
// https://youtu.be/ygL_xcavzQ4?t=3355