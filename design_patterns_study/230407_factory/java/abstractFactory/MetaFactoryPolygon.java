package abstractFactory;

// This is the factory that will generate other factories.
// here we chose the color then the child factories we'll chose the
// numSides.
public class MetaFactoryPolygon{

    public static FactoryColorInterface create_factory(String color){
        switch(color) {
        case "blue":
            return new FactoryBluePolygon();
        case "red":
            return new FactoryRedPolygon();
        case "green":
            return new FactoryGreenPolygon();
        default:
            return null;
        }
    }

}
