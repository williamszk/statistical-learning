import polygon
import abstract


def main():
    print("== From calling classes directly ====================================")
    polygon.BlueTriangle().get()
    polygon.BlueRectangle().get()
    polygon.BluePentagon().get()

    polygon.RedTriangle().get()
    polygon.RedRectangle().get()
    polygon.RedPentagon().get()

    polygon.GreenTriangle().get()
    polygon.GreenRectangle().get()
    polygon.GreenPentagon().get()

    print("== From calling the factoryMethod ====================================")

    # factory.FactoryPolygon().create(3).get()
    # factory.FactoryPolygon().create(4).get()
    # factory.FactoryPolygon().create(5).get()
    abstract.AbstractFactoryPolygon().create_factory("blue").create(3).get()
    abstract.AbstractFactoryPolygon().create_factory("blue").create(4).get()
    abstract.AbstractFactoryPolygon().create_factory("blue").create(5).get()

    abstract.AbstractFactoryPolygon().create_factory("red").create(3).get()
    abstract.AbstractFactoryPolygon().create_factory("red").create(4).get()
    abstract.AbstractFactoryPolygon().create_factory("red").create(5).get()

    abstract.AbstractFactoryPolygon().create_factory("green").create(3).get()
    abstract.AbstractFactoryPolygon().create_factory("green").create(4).get()
    abstract.AbstractFactoryPolygon().create_factory("green").create(5).get()

if __name__ == "__main__":
    main()
