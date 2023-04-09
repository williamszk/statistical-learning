package abstractFactory;

public class Main{
    public static void main(String[] args) {

        System.out.println("Hello World");

        System.out.println("== From calling classes directly ====================================");
        BlueTriangle tri = new BlueTriangle();
        tri.get();

        BlueRectangle rec = new BlueRectangle();
        rec.get();

        BluePentagon pen = new BluePentagon();
        pen.get();


        RedTriangle tri2 = new RedTriangle();
        tri2.get();

        RedRectangle rec2 = new RedRectangle();
        rec2.get();

        RedPentagon pen2 = new RedPentagon();
        pen2.get();


        GreenTriangle tri3 = new GreenTriangle();
        tri3.get();

        GreenRectangle rec3 = new GreenRectangle();
        rec3.get();

        GreenPentagon pen3 = new GreenPentagon();
        pen3.get();

        System.out.println("== From calling the abstractFactory ====================================");

        Polygon tri4 = MetaFactoryPolygon.create_factory("blue").create(3);
        tri4.get();

        Polygon rec4 = MetaFactoryPolygon.create_factory("blue").create(4);
        rec4.get();

        Polygon pen4 = MetaFactoryPolygon.create_factory("blue").create(5);
        pen4.get();


        Polygon tri5 = MetaFactoryPolygon.create_factory("red").create(3);
        tri5.get();

        Polygon rec5 = MetaFactoryPolygon.create_factory("red").create(4);
        rec5.get();

        Polygon pen5 = MetaFactoryPolygon.create_factory("red").create(5);
        pen5.get();


        Polygon tri6 = MetaFactoryPolygon.create_factory("green").create(3);
        tri6.get();

        Polygon rec6 = MetaFactoryPolygon.create_factory("green").create(4);
        rec6.get();

        Polygon pen6 = MetaFactoryPolygon.create_factory("green").create(5);
        pen6.get();
    }
}
