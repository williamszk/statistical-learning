// This script is used to check how we would have to deal with a 2nd order
// branching if we do not use an abstract factory pattern.

// In here we'll use a bunch of if else to achieve the same factory pattern for all 
// 9 structs
// This way works if the interface of all structs is the same for all 9 structs.
// - BlueTriangle
// - BlueRectangle
// - BluePentagon
// - RedTriangle
// - RedRectangle
// - RedPentagon
// - GreenTriangle
// - GreenRectangle
// - GreenPentagon

// For each color we could have a different interface
// for each shape we could have a different interface

fn main() {
    println!("Hello World");
    println!("== From calling classes directly ====================================");

    let tri = BlueTriangle {};
    tri.get();

    let rec = BlueRectangle {};
    rec.get();

    let pen = BluePentagon {};
    pen.get();


    let tri = RedTriangle {};
    tri.get();

    let rec = RedRectangle {};
    rec.get();

    let pen = RedPentagon {};
    pen.get();


    let tri = GreenTriangle {};
    tri.get();

    let rec = GreenRectangle {};
    rec.get();

    let pen = GreenPentagon {};
    pen.get();

    println!("== From calling the abstract factoryMethod ====================================");

    FactoryPolygon::create("blue", 3).get();
    FactoryPolygon::create("blue", 4).get();
    FactoryPolygon::create("blue", 5).get();

    FactoryPolygon::create("red", 3).get();
    FactoryPolygon::create("red", 4).get();
    FactoryPolygon::create("red", 5).get();

    FactoryPolygon::create("green", 3).get();
    FactoryPolygon::create("green", 4).get();
    FactoryPolygon::create("green", 5).get();

}

pub trait Polygon{
    fn get(&self);
}

pub struct BlueTriangle {}

impl Polygon for BlueTriangle {
    fn get(&self) {
        println!("Hello from BlueTriangle");
    }
}

pub struct RedTriangle {}

impl Polygon for RedTriangle {
    fn get(&self) {
        println!("Hello from RedTriangle");
    }
}

pub struct GreenTriangle {}

impl Polygon for GreenTriangle {
    fn get(&self) {
        println!("Hello from GreenTriangle");
    }
}

pub struct BlueRectangle {}

impl Polygon for BlueRectangle {
    fn get(&self) {
        println!("Hello from BlueRectangle");
    }
}

pub struct RedRectangle {}

impl Polygon for RedRectangle {
    fn get(&self) {
        println!("Hello from RedRectangle");
    }
}

pub struct GreenRectangle {}

impl Polygon for GreenRectangle {
    fn get(&self) {
        println!("Hello from GreenRectangle");
    }
}

pub struct BluePentagon {}

impl Polygon for BluePentagon {
    fn get(&self) {
        println!("Hello from BluePentagon");
    }
}

pub struct RedPentagon {}

impl Polygon for RedPentagon {
    fn get(&self) {
        println!("Hello from RedPentagon");
    }
}

pub struct GreenPentagon {}

impl Polygon for GreenPentagon {
    fn get(&self) {
        println!("Hello from GreenPentagon");
    }
}


struct FactoryPolygon{}

// This didn't took too much work...
// but it would be hard to include more types in this way of building 2 layered
// branches...
// Using 2 layers of factories, with a meta-factory  makes things a little more
// manageable for when we want to change the structs that are returned.
impl FactoryPolygon{

    fn create(color: &str,num_sides:u32) -> Box<dyn Polygon>{
        if color == "blue" && num_sides == 3 {
            Box::new(BlueTriangle{})
        } else if color == "blue" && num_sides == 4{
            Box::new(BlueRectangle{})
        } else if color == "blue" && num_sides == 5 {
            Box::new(BluePentagon{})
        } else if color == "red" && num_sides == 3 {
            Box::new(RedTriangle{})
        } else if color == "red" && num_sides == 4{
            Box::new(RedRectangle{})
        } else if color == "red" && num_sides == 5 {
            Box::new(RedPentagon{})
        } else if color == "green" && num_sides == 3 {
            Box::new(GreenTriangle{})
        } else if color == "green" && num_sides == 4{
            Box::new(GreenRectangle{})
        } else if color == "green" && num_sides == 5 {
            Box::new(GreenPentagon{})
        } else {
            panic!("Sorry, we have no option of Polygon for the number passed");
        }
    }

}

