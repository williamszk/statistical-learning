import polygon
import factory


def main():
    print("== From calling classes directly ====================================")
    polygon.Triangle().get()
    polygon.Rectangle().get()
    polygon.Pentagon().get()

    print("== From calling the factoryMethod ====================================")

    factory.FactoryPolygon().create(3).get()
    factory.FactoryPolygon().create(4).get()
    factory.FactoryPolygon().create(5).get()


if __name__ == "__main__":
    main()
