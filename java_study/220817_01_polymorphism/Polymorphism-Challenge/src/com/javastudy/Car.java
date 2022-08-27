package com.javastudy;

public class Car {

    private String name;
    private boolean engine;
    private int cylinders;
    private int wheels;

    public Car(String name, int cylinders) {
        this.engine = true;
        this.cylinders = cylinders;
        this.wheels = 4;
    }


    public String getName() {
        return name;
    }

    public boolean isEngine() {
        return engine;
    }

    public int getCylinders() {
        return cylinders;
    }

    public int getWheels() {
        return wheels;
    }

    public void startEngine() {
        System.out.println("Engine started");
    }

    public void accelerate() {
        System.out.println("Accelerating car");
    }

    public void brake() {
        System.out.println("Activating wheel brakes");
    }
}
