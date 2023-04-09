package factoryMethod;

public class Main{
    public static void main(String[] args) {

        System.out.println("Hello World");

        System.out.println("== From calling classes directly ====================================");
        Triangle tri = new Triangle();
        tri.get();

        Rectangle rec = new Rectangle();
        rec.get();

        Pentagon pen = new Pentagon();
        pen.get();

        System.out.println("== From calling the factoryMethod ====================================");

        Polygon tri2 = PolygonFactory.create(3);
        tri2.get();

        Polygon rec2 = PolygonFactory.create(4);
        rec2.get();

        Polygon pen2 = PolygonFactory.create(5);
        pen2.get();

    }
}
