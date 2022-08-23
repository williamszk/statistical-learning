package com.javastudy;

public class FiestaFord extends Car {

    public FiestaFord() {
        super("Fiesta - Ford", 1000);
    }

    public void startEngine() {
        System.out.println("Fiesta Ford -> Engine started");
    }

    public void accelerate() {
        System.out.println("Fiesta Ford -> Accelerating car");
    }

    public void brake() {
        System.out.println("Fiesta Ford -> Activating wheel brakes");
    }

}
