
package abstractFactory;

public class FactoryRedPolygon implements FactoryColorInterface{
    public Polygon create(int numSides){
        switch(numSides) {
        case 3:
            return new RedTriangle();
        case 4:
            return new RedRectangle();
        case 5:
            return new RedPentagon();
        default:
            return null;
        }
    }
}