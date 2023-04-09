fn main() {
    println!("Hello World");
    println!("== From calling classes directly ====================================");

    let tri = Triangle {};
    tri.get();

    let rec = Rectangle {};
    rec.get();

    let pen = Pentagon {};
    pen.get();

    println!("== From calling the factoryMethod using enums =======================");

    let tri2 = factory_polygon(3);


}

trait Polygon {
    fn get(&self);
}

struct Triangle {}

impl Polygon for Triangle {
    fn get(&self) {
        println!("Hello from Triangle");
    }
}

struct Rectangle {}

impl Polygon for Rectangle {
    fn get(&self) {
        println!("Hello from Rectangle");
    }
}

struct Pentagon {}

impl Polygon for Pentagon {
    fn get(&self) {
        println!("Hello from Pentagon");
    }
}



// struct FactoryPolygon{}

// impl FactoryPolygon{
//     fn create(numSides:u32) -> impl Polygon{
//         // Triangle{}
//         if numSides == 3 {
//             Triangle{}
//         } else if numSides == 4{
//             Rectangle{}
//         } else if numSides == 5 {
//             Pentagon{}
//         } else {
//             panic!("Error");
//         }
//     }
// }

// This doesn't work... I'll try to use enum
#[derive(Debug)]
enum PolygonEnum{
    Triangle,
    Rectangle,
    Pentagon,
}

fn factory_polygon(num_sides: u32) -> PolygonEnum{
    if num_sides == 3 {
        PolygonEnum::Triangle{}
    } else if num_sides == 4{
        PolygonEnum::Rectangle{}
    } else if num_sides == 5 {
        PolygonEnum::Pentagon{}
    } else {
        panic!("Error");
    }
}

// Using enum in this situation is not a good idea
// because we can't use the method specific from a trait...
// Enums are more generic then returning a trait.



