package com.javastudy;

public class UnoFiat extends Car {

    public UnoFiat() {
        super("Uno - Fiat", 700);
    }

    @Override
    public void startEngine() {
        System.out.println("Fiat Uno -> Engine started");
    }

    @Override
    public void accelerate() {
        System.out.println("Fiat Uno -> Accelerating car");
    }

    @Override
    public void brake() {
        System.out.println("Fiat Uno -> Activating wheel brakes");
    }

}
