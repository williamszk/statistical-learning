
fn main() {
    println!("Hello World");
    println!("== From calling classes directly ====================================");

    let tri = Triangle {};
    tri.get();

    let rec = Rectangle {};
    rec.get();

    let pen = Pentagon {};
    pen.get();

    println!("== From calling the factoryMethod ====================================");

    let tri = factory_polygon(3);
    tri.get();

    let rec = factory_polygon(4);
    rec.get();

    let pen = factory_polygon(5);
    pen.get();
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

// We are using a function instead of a method here.
fn factory_polygon(num_sides: u32)-> Box<dyn Polygon>{
    match num_sides {
        3=>Box::new(Triangle{}),
        4=>Box::new(Rectangle{}),
        5=>Box::new(Pentagon{}),
        _=>panic!("Error"),
    }
}


