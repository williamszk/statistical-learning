package factoryMethod;

public class PolygonFactory{

    public static Polygon create(int numSides){
        if (numSides == 3){
            return new Triangle();
        } else if (numSides == 4){
            return new Rectangle();
        } else if (numSides == 5){
            return new Pentagon();
        } else {
            return null;
        }
    }
}