use crate::polygon::Polygon;

pub trait FactoryShapePolygonTrait {
    fn create(&self, num_sides: u32) -> Box<dyn Polygon>;
}