use crate::factory_shape_polygon_trait::FactoryShapePolygonTrait;
use crate::factory_polygon::{FactoryBluePolygon, FactoryRedPolygon, FactoryGreenPolygon};

// Let's create the two-layered factory pattern:
pub struct MetaFactoryPolygonColor {}

impl MetaFactoryPolygonColor {
    // Given that we didn't included a &self in the method, this is a static method
    // then we just call it by
    // MetaFactoryPolygonColor::create_factory()
    pub fn create_factory(color: &str) -> Box<dyn FactoryShapePolygonTrait> {
        match color {
            "blue" => Box::new(FactoryBluePolygon {}),
            "red" => Box::new(FactoryRedPolygon {}),
            "green" => Box::new(FactoryGreenPolygon {}),
            _ => panic!("Sorry, and error happened."),
        }
    }
}
