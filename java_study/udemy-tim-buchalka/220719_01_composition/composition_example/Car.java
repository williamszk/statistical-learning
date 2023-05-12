package composition_example;

public class Car extends Vehicle {
    private int doors;
    private int engineCapacity;

    public Car(String name, int doors, int engineCapacity) {
        super(name);
        this.doors = doors;
        this.engineCapacity = engineCapacity;
    }

    public int getDoors() {
        return doors;
    }

    public int getEngineCapacity() {
        return engineCapacity;
    }
}
