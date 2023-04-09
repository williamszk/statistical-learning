
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