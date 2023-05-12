package com.javastudy;

public class Holden extends Car{

    public Holden(int cylinders, String name) {
        super(cylinders, name);
    }


    public String startEngine(){
        return this.getClass().getSimpleName() + " -> startEngine()";
    }

    public String accelerate(){
        return this.getClass().getSimpleName() + " -> accelerate()";
    }

    public String brake(){
        return this.getClass().getSimpleName() + " -> brake()";
    }
}
