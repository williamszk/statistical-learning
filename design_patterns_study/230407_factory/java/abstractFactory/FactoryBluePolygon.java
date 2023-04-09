package abstractFactory;

public class FactoryBluePolygon implements FactoryColorInterface{

    public Polygon create(int numSides){
        switch(numSides) {
        case 3:
            return new BlueTriangle();
        case 4:
            return new BlueRectangle();
        case 5:
            return new BluePentagon();
        default:
            return null;
        }
    }

}
