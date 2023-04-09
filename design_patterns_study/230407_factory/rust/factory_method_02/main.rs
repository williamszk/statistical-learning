use std::any::type_name;

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

    // let tri2 = factory_polygon(3);
    let tri = FactoryPolygon{}.create(3);
    println!("{}", type_of(&tri));
    tri.get();

    let rec = FactoryPolygon{}.create(4);
    rec.get();

    let pen = FactoryPolygon{}.create(5);
    pen.get();

    FactoryPolygon{}.create(6);

}

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
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

// having a struct wrapping around the factory method could make it easier for
// creating the abstract factory method
struct FactoryPolygon{}

impl FactoryPolygon{

    fn create(&self, num_sides:u32) -> Box<dyn Polygon>{
        // Triangle{}
        if num_sides == 3 {
            Box::new(Triangle{})
        } else if num_sides == 4{
            Box::new(Rectangle{})
        } else if num_sides == 5 {
            Box::new(Pentagon{})
        } else {
            panic!("Sorry, we have no option of Polygon for the number passed");
        }
    }

}






