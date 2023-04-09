use crate::polygon::{BlueTriangle, BlueRectangle, BluePentagon, RedTriangle, RedRectangle, RedPentagon, GreenTriangle, GreenRectangle, GreenPentagon, Polygon};
use crate::factory_shape_polygon_trait::FactoryShapePolygonTrait;

pub struct FactoryBluePolygon {}

impl FactoryShapePolygonTrait for FactoryBluePolygon {
    fn create(&self, num_sides: u32) -> Box<dyn Polygon> {
        match num_sides {
            3 => Box::new(BlueTriangle {}),
            4 => Box::new(BlueRectangle {}),
            5 => Box::new(BluePentagon {}),
            _ => panic!("Sorry, and error happened."),
        }
    }
}

pub struct FactoryRedPolygon {}

impl FactoryShapePolygonTrait for FactoryRedPolygon {
    fn create(&self, num_sides: u32) -> Box<dyn Polygon> {
        match num_sides {
            3 => Box::new(RedTriangle {}),
            4 => Box::new(RedRectangle {}),
            5 => Box::new(RedPentagon {}),
            _ => panic!("Error!"),
        }
    }
}


pub struct FactoryGreenPolygon {}

impl FactoryShapePolygonTrait for FactoryGreenPolygon {
    fn create(&self, num_sides: u32) -> Box<dyn Polygon> {
        match num_sides {
            3 => Box::new(GreenTriangle {}),
            4 => Box::new(GreenRectangle {}),
            5 => Box::new(GreenPentagon {}),
            _ => panic!("Sorry, and error happened."),
        }
    }
}
