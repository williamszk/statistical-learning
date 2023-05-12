package com.javastudy;

public class GolVW extends Car {

    public GolVW() {
        super("Gol - Volkswagen", 1200);
    }

    @Override
    public void startEngine() {
        System.out.println("Gol VW -> Engine started");
    }

    @Override
    public void accelerate() {
        System.out.println("Gol VW -> Accelerating car");
    }

    @Override
    public void brake() {
        System.out.println("Gol VW -> Activating wheel brakes");
    }
}
