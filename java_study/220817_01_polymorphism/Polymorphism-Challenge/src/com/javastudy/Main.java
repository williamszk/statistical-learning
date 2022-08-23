package com.javastudy;

public class Main {

    public static void main(String[] args) {

        FiestaFord myCar01 = new FiestaFord();
        startEngine(myCar01);

        UnoFiat myCar02 = new UnoFiat();
        startEngine(myCar02);

        GolVW myCar03 = new GolVW();
        startEngine(myCar03);

        Car myCar04 = new Car("My nameless car", 1000);
        startEngine(myCar04);


    }


    public static void startEngine(Car car) {
        car.startEngine();
    }

}
