
package abstractFactory;

public class FactoryGreenPolygon implements FactoryColorInterface{
    public Polygon create(int numSides){
        switch(numSides) {
        case 3:
            return new GreenTriangle();
        case 4:
            return new GreenRectangle();
        case 5:
            return new GreenPentagon();
        default:
            return null;
        }
    }
}