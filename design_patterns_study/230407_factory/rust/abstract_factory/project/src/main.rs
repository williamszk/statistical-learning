
mod meta_factory_polygon_color;
mod factory_shape_polygon_trait;
mod factory_polygon;
mod polygon;
use crate::meta_factory_polygon_color::MetaFactoryPolygonColor;
use crate::polygon::{BlueTriangle, BlueRectangle, BluePentagon, RedTriangle, RedRectangle, RedPentagon, GreenTriangle, GreenRectangle, GreenPentagon, Polygon};

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

    let tri = MetaFactoryPolygonColor::create_factory("blue").create(3);
    tri.get();

    let tri = MetaFactoryPolygonColor::create_factory("red").create(3);
    tri.get();

    let tri = MetaFactoryPolygonColor::create_factory("green").create(3);
    tri.get();

    let pol = MetaFactoryPolygonColor::create_factory("blue").create(4);
    pol.get();

}


// I have the option to create interfaces for:
// 1. color (Blue, Red, Green)
// 2. shape (Triangle, Rectangle, Pentagon)
// But that is not a relevant thing unless they have different
// functions and signatures...
// In my case I just want to have two dimensions of differentiation.

// I could just build two layers of factories.
// The first layer is a factory that creates factories.
// and the second layer is a factory that creates concrete classes.

// If I saw fit, instead of creating two layers of factories, we could
// just use one layer and include all possible 9 concrete classes in there.

// Let's create the two-layered factory pattern:

